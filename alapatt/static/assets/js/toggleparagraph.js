function toggleParagraph(element) {
    const img = element.querySelector('img');
    const paragraph = element.querySelector('.hidden-paragraph');

    if (img.style.display !== 'none') {
        img.style.display = 'none';
        paragraph.style.display = 'block';
    } else {
        img.style.display = 'block';
        paragraph.style.display = 'none';
    }
}