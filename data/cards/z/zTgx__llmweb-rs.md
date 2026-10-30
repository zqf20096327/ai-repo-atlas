# zTgx/llmweb-rs

⭐ 16 · Rust · MIT · 推送 2026-05-25 · [GitHub](https://github.com/zTgx/llmweb-rs) · 个人维护

**Rust 网页结构化数据提取库：headless Chrome + LLM 一次调用得类型化结果**

面向 Rust 开发者的网页提取库：通过 headless Chrome 打开页面或直接读入 HTML 字符串，经 5 种预处理模式（html/markdown/text/image 等）后调用一次 LLM，返回按 schema 定义的类型化结构数据；支持流式部分 JSON 输出。另提供代码生成机制——由 LLM 生成 JS 提取器或 CSS 选择器 recipe，后续重放可零 LLM 成本、纯 Rust 执行。LLM 端通过 LlmWeb::with_client 接入任意 OpenAI 兼容端点。以 crate 形式发布，另有 cargo install 的 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- exec/exec_on_tab/exec_on_html 一次 LLM 调用返回类型化结果
- generate 生成 JS 提取器或 CSS recipe，重放时零 LLM 成本
- 5 种预处理模式，含面向视觉模型的 base64 截图
- 任意 OpenAI 兼容端点接入，支持流式部分 JSON

## 适用场景

- 把搜索结果、帖子列表等网页提取为结构化数据
- 先由 LLM 生成提取脚本，再离线低成本批量抓取
- 在 Rust 项目中集成带 schema 约束的网页解析

## 场景标签

`网页抓取` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Extract any webpage to structured data — headless Chrome + LLM.**
> L39: - **Extract** — `exec` / `exec_on_tab` / `exec_on_html`: one LLM call → typed `R`.
> L44: - **Multi-provider** — any OpenAI-compatible endpoint via `LlmWeb::with_client`.

## 星数曲线

```mermaid
xychart-beta
    title "zTgx/llmweb-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `3488c2fc69e9` · [字段定义](../../DATASET.md)*
