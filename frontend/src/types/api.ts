export interface Category {
    id: number;
    name: string;
    slug: string;
    color: string;
    description?: string;
}

export interface Tag {
    id: number;
    name: string;
    slug: string;
    color: string;
}

export interface ArticlePreview {
    id: number;
    title: string;
    slug: string;
    excerpt: string;
    cover_image: string | null;
    is_featured: boolean;
    is_published: boolean;
    views_count: number;
    reading_time: number;
    published_at: string | null;
    categories: Category[];
    tags: Tag[];
}

export interface ArticleResponse extends ArticlePreview {
    content: TipTapDoc;
    author_id: number;
    created_at: string;
    updated_at: string;
}

export interface ArticleListResponse {
    items: ArticlePreview[];
    total: number;
    page: number;
    per_page: number;
    pages: number;
}

export interface TipTapDoc {
    type: string;
    content?: TipTapNode[];
}

export interface TipTapNode {
    type: string;
    text?: string;
    content?: TipTapNode[];
    marks?: TipTapMark[];
    attrs?: Record<string, any>;
}

export interface TipTapMark {
    type: string;
    attrs?: Record<string, any>;
}
