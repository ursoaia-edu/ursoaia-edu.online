import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { fetchApi } from '../lib/api';
import type { ArticleListResponse } from '../types/api';

export async function GET(context: APIContext) {
    const data = await fetchApi<ArticleListResponse>('/articles?per_page=50');
    const articles = data?.items || [];

    return rss({
        title: 'Ursoaia Edu',
        description: 'Portal educațional cu resurse de învățare pentru elevi și studenți',
        site: context.site!,
        items: articles.map((article) => ({
            title: article.title,
            description: article.excerpt,
            link: `/articles/${article.slug}`,
            pubDate: article.published_at ? new Date(article.published_at) : undefined,
        })),
        customData: `<language>ro-RO</language>`,
    });
}
