const projectContainers = {
  all: document.querySelector("#all-projects"),
  filters: document.querySelector("#project-filters"),
};

const navToggle = document.querySelector(".nav-toggle");
const siteNav = document.querySelector(".site-nav");
const year = document.querySelector("#year");

let projects = [];
let activeCategory = "All";

if (year) {
  year.textContent = new Date().getFullYear();
}

if (navToggle && siteNav) {
  navToggle.addEventListener("click", () => {
    const isOpen = siteNav.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  siteNav.addEventListener("click", (event) => {
    if (event.target.matches("a")) {
      siteNav.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    }
  });
}

function createBadge(label, className = "badge") {
  const span = document.createElement("span");
  span.className = className;
  span.textContent = label;
  return span;
}

function createProjectCard(project) {
  const article = document.createElement("article");
  article.className = "project-card";

  if (project.image) {
    const imageWrap = document.createElement("div");
    imageWrap.className = "project-image-wrap";

    const image = document.createElement("img");
    image.className = "project-image";
    image.src = project.image;
    image.alt = project.title;
    image.loading = "lazy";

    imageWrap.appendChild(image);
    article.appendChild(imageWrap);
  }

  const meta = document.createElement("div");
  meta.className = "project-meta";

  if (project.year) {
    meta.appendChild(createBadge(project.year));
  }

  if (project.status) {
    meta.appendChild(createBadge(project.status));
  }

  if (Array.isArray(project.categories)) {
    project.categories.forEach((category) => {
      meta.appendChild(createBadge(category));
    });
  }

  const title = document.createElement("h3");
  title.textContent = project.title;

  article.append(meta, title);

  if (project.subtitle) {
    const subtitle = document.createElement("p");
    subtitle.className = "project-subtitle";
    subtitle.textContent = project.subtitle;
    article.appendChild(subtitle);
  }

  const description = document.createElement("p");
  description.textContent = project.description;
  article.appendChild(description);

  if (Array.isArray(project.highlights) && project.highlights.length > 0) {
    const highlights = document.createElement("ul");
    highlights.className = "project-highlights";

    project.highlights.slice(0, 2).forEach((highlight) => {
      const item = document.createElement("li");
      item.textContent = highlight;
      highlights.appendChild(item);
    });

    article.appendChild(highlights);
  }

  if (Array.isArray(project.technologies) && project.technologies.length > 0) {
    const tagRow = document.createElement("div");
    tagRow.className = "tag-row";

    project.technologies.forEach((technology) => {
      tagRow.appendChild(createBadge(technology, "tag"));
    });

    article.appendChild(tagRow);
  }

  const links = document.createElement("div");
  links.className = "project-links";

  if (project.links?.github) {
    const githubLink = document.createElement("a");
    githubLink.className = "text-link";
    githubLink.href = project.links.github;
    githubLink.target = "_blank";
    githubLink.rel = "noreferrer";
    githubLink.textContent = "Repository";
    links.appendChild(githubLink);
  }

  if (project.links?.report) {
    const reportLink = document.createElement("a");
    reportLink.className = "text-link";
    reportLink.href = project.links.report;
    reportLink.target = "_blank";
    reportLink.rel = "noreferrer";
    reportLink.textContent = "Report";
    links.appendChild(reportLink);
  }

  if (project.links?.demo) {
    const demoLink = document.createElement("a");
    demoLink.className = "text-link";
    demoLink.href = project.links.demo;
    demoLink.target = "_blank";
    demoLink.rel = "noreferrer";
    demoLink.textContent = "Demo";
    links.appendChild(demoLink);
  }

  if (project.links?.website) {
    const websiteLink = document.createElement("a");
    websiteLink.className = "text-link";
    websiteLink.href = project.links.website;
    websiteLink.target = "_blank";
    websiteLink.rel = "noreferrer";
    websiteLink.textContent = "Website";
    links.appendChild(websiteLink);
  }

  if (links.children.length > 0) {
    article.appendChild(links);
  }

  return article;
}

function getVisibleProjects() {
  if (activeCategory === "All") {
    return projects;
  }

  return projects.filter((project) => {
    return Array.isArray(project.categories) && project.categories.includes(activeCategory);
  });
}

function renderProjects() {
  const visibleProjects = getVisibleProjects().sort(compareProjectsByOrder);

  if (!projectContainers.all) {
    return;
  }

  projectContainers.all.replaceChildren(...visibleProjects.map(createProjectCard));
}

function renderFilters() {
  if (!projectContainers.filters) {
    return;
  }

  const categories = [
    "All",
    ...new Set(projects.flatMap((project) => project.categories || [])),
  ];

  const buttons = categories.map((category) => {
    const button = document.createElement("button");
    button.className = `filter-button${category === activeCategory ? " active" : ""}`;
    button.type = "button";
    button.textContent = category;

    button.addEventListener("click", () => {
      activeCategory = category;
      renderFilters();
      renderProjects();
    });

    return button;
  });

  projectContainers.filters.replaceChildren(...buttons);
}

async function loadProjects() {
  try {
    const response = await fetch("data/projects.json");

    if (!response.ok) {
      throw new Error(`Unable to load projects: ${response.status}`);
    }

    const loadedProjects = await response.json();
    projects = Array.isArray(loadedProjects) ? loadedProjects.sort(compareProjectsByOrder) : [];

    renderFilters();
    renderProjects();
  } catch (error) {
    if (projectContainers.all) {
      projectContainers.all.textContent = "Projects are currently unavailable.";
    }

    console.error(error);
  }
}

function compareProjectsByOrder(a, b) {
  const orderA = typeof a.order === "number" ? a.order : 999;
  const orderB = typeof b.order === "number" ? b.order : 999;
  return orderA - orderB;
}

loadProjects();
