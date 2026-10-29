# spatie/laravel-markdown-response

⭐ 83 · PHP · MIT · 推送 2026-10-22 · [GitHub](https://github.com/spatie/laravel-markdown-response) · [官网](https://spatie.be/docs/laravel-markdown-response) · 组织维护

**Laravel 包：向 AI 代理与爬虫输出页面的 Markdown 版本**

为 Laravel 应用提供的中间件包：当请求带 Accept: text/markdown 头、匹配已知 AI 用户代理模式或使用 .md URL 后缀时，将 HTML 页面转换为 Markdown 返回。转换基于驱动（本地 PHP 或 Cloudflare Workers AI），结果缓存，转换前可对 HTML 预处理；也可通过 Markdown 门面直接调用 convert() 进行转换或编写转换测试。面向使用 Laravel 的开发者，以 Composer 包分发，文档见官方站点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Accept 头、AI UA 模式或 .md 后缀三种方式检测 Markdown 请求
- 驱动式转换（本地 PHP 或 Cloudflare Workers AI）
- 转换结果缓存与 HTML 预处理钩子
- 提供 Markdown 门面直接转换与测试辅助

## 适用场景

- 让 AI 代理和爬虫获得站点的干净 Markdown 内容
- 以 /about.md 形式向用户提供页面 Markdown 版
- 在测试中验证页面的 Markdown 转换结果

## 场景标签

 · 领域:Web 开发/内容交付

## 证据(README 行号)

> L7:  Serve markdown versions of your HTML pages to AI agents and bots
> L14: AI agents increasingly consume web content. This package lets your Laravel app serve markdown versions of HTML page

## 星数曲线

```mermaid
xychart-beta
    title "spatie/laravel-markdown-response 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 82 --> 84
    line [83, 83]
```

2026-10-18 83 → 2026-10-29 83（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `210a2c643bfc` · [字段定义](../../DATASET.md)*
