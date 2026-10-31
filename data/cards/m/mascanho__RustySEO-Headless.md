# mascanho/RustySEO-Headless

⭐ 14 · Rust · 推送 2026-08-31 · [GitHub](https://github.com/mascanho/RustySEO-Headless) · [官网](https://rustyseo.com) · 组织维护

**终端里的网站 SEO 审计工具：爬取分析并给出 AI 建议**

基于 Rust 的 TUI 应用，以 Headless Chrome 做 JavaScript 渲染爬取，自动检测 15+ 类 SEO 问题（4xx/5xx、标题与 meta 长度、缺失 H1 与 alt 文本、重定向链、Core Web Vitals 等），提供表格、图表与树状站点结构可视化，可导出 CSV/JSON/PDF。内置 AI 聊天，支持 OpenAI GPT-4、Gemini 与自定义端点，基于网站数据给出建议。配置采用 TOML 文件，爬取与分析在本地完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Headless Chrome JavaScript 渲染爬取，支持 sitemap/robots.txt 解析与限速
- 自动检测 15+ 类 SEO 问题并给出 Core Web Vitals 指标
- AI 聊天集成 OpenAI GPT-4、Gemini 与自定义端点
- CSV/JSON/PDF 导出与 TOML 持久化配置

## 适用场景

- 在终端中对大型网站做技术 SEO 审计
- 在云端服务器上无人值守地运行 SEO 分析
- 就自己的爬取数据向 AI 询问优化建议

## 场景标签

 · 领域:开发工具/SEO 营销

## 证据(README 行号)

> L22: - **🎯 Comprehensive Analysis**: Detects 15+ types of SEO issues automatically
> L24: - **🤖 AI-Powered Insights**: Integrated AI chat for SEO recommendations
> L51: - **Smart Recommendations**: AI-powered SEO suggestions

## 星数曲线

```mermaid
xychart-beta
    title "mascanho/RustySEO-Headless 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4c500e188152` · [字段定义](../../DATASET.md)*
