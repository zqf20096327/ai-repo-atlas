# sebastienrousseau/static-site-generator

⭐ 58 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/sebastienrousseau/static-site-generator) · [官网](https://docs.static-site-generator.com/) · 个人维护

**面向无障碍与安全的 Rust 静态网站生成器，含本地 LLM 内容管线**

以 Rust 编写的静态网站生成器：读取 Markdown、YAML frontmatter 与 MiniJinja 模板，生成生产可用的 HTML。内建 32 插件管线，覆盖 SEO、WCAG 2.2 AA 无障碍校验、CSP/SRI 加固、原生 JS/CSS 压缩、28 语言 i18n、RSS/Atom、CycloneDX SBOM 生成。AI 部分（--ai-fix）通过本地 LLM（Ollama）审计内容可读性、诊断失败文件、生成修复并验证，可自动生成 alt 文本与 JSON-LD。支持 10 万+ 页面的受限内存批处理编译与 WebAssembly 边缘运行时目标。安装方式包括 cargo install、预编译二进制脚本与源码构建（Rust 1.89.0+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WCAG 2.2 AA 校验作为构建阶段执行，输出合规矩阵，STRICT_A11Y 可选失败门控
- Agentic LLM 管线（--ai-fix）：经 Ollama 本地模型审计、诊断、修复并验证内容可读性
- CSP 构建期提取与 SRI 哈希生成，zero unsafe-inline
- 受限内存批处理编译支持 100K+ 页面站点，--max-memory 可配置

## 适用场景

- 生成满足 WCAG 2.2 AA 与 CSP/SRI 安全要求的生产级静态站点
- 用本地 LLM 自动审计并修复内容可读性、生成 alt 文本与元描述
- 构建 10 万页以上规模的多语言站点（28 语言 i18n 与 hreflang）
- 部署到 Cloudflare Workers 或 Vercel Edge 等边缘运行时

## 场景标签

 · 领域:Web 开发/静态站点工具

## 证据(README 行号)

> L5:  AI-augmented, accessibility-first static site generator built in Rust.
> L74: - **Agentic AI pipeline** -- audit, diagnose, fix, and verify content readability via local LLM
> L169: |**AI Pipeline**|Agentic LLM pipeline (`--ai-fix`): audit content readability, diagnose failing files, generate fi

## 星数曲线

```mermaid
xychart-beta
    title "sebastienrousseau/static-site-generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-30 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `55bc23fa9170` · [字段定义](../../DATASET.md)*
