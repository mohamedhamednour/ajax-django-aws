function ajaxGet(url, callback) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            callback(JSON.parse(xhr.responseText));
        }
    };
    xhr.send();
}

function createCheckbox(id, label, className, onChange) {
    const div = document.createElement('div');
    div.className = className;

    const input = document.createElement('input');
    input.type = 'checkbox';
    input.id = id;
    input.onchange = onChange;

    const labelElement = document.createElement('label');
    labelElement.htmlFor = id;
    labelElement.textContent = label;

    div.appendChild(input);
    div.appendChild(labelElement);

    return div;
}

const categoryContainer = document.getElementById('category-container');
const subcategoryContainer = document.getElementById('subcategory-container');
const subcategoryHeader = document.getElementById('subcategories');
const BASEURL = 'http://127.0.0.1:6006/api/';

function fetchCategories() {
    ajaxGet(`${BASEURL}categories/`, function (categories) {
        categories.forEach(category => {
            const div = createCheckbox(
                `category-${category.id}`,
                `Category ${category.name}`,
                `category-group`,
                function () {
                    if (this.checked) {
                        subcategoryHeader.style.opacity = 1;
                        fetchSubcategories(category.id);
                    } else {
                        const toRemove = document.querySelectorAll(`.subcategory-group-${category.id}`);
                        toRemove.forEach(el => el.remove());
                        if (document.querySelectorAll('.subcategory-group').length === 0) {
                            subcategoryHeader.style.opacity = 0;
                        }
                    }
                }
            );
            categoryContainer.appendChild(div);
        });
    });
}

function fetchSubcategories(categoryId) {
    const url = `${BASEURL}subcategories/?category=${categoryId}`;
    ajaxGet(url, function (subcategories) {
        subcategories.forEach(sub => {
            const div = createCheckbox(
                `subcategory-${sub.id}`,
                `Subcategory ${sub.name}`,
                `subcategory-group subcategory-group-${categoryId}`,
                function () {
                    if (this.checked) {
                        fetchSubSubcategories(sub.id, div);
                    } else {
                        const toRemove = div.querySelectorAll('.sub-subcategory-group');
                        toRemove.forEach(el => el.remove());
                    }
                }
            );
            subcategoryContainer.appendChild(div);
        });
    });
}

function fetchSubSubcategories(subcategoryId, parentDiv) {
    const url = `${BASEURL}subcategories/?parent=${subcategoryId}`;
    ajaxGet(url, function (subSubcategories) {
        subSubcategories.forEach(subSub => {
            const subSubDiv = document.createElement('div');
            subSubDiv.textContent = ` ${subSub.name}`;
            subSubDiv.className = 'sub-subcategory-group';
            subSubDiv.style.marginLeft = '20px'; 
            parentDiv.appendChild(subSubDiv); 
        });
    });
}

fetchCategories();
