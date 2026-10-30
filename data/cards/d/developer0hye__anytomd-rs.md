# developer0hye/anytomd-rs

⭐ 58 · Rust · Apache-2.0 · 推送 2026-09-22 · [GitHub](https://github.com/developer0hye/anytomd-rs) · 个人维护

**纯 Rust 文档转 Markdown 工具/库，面向 LLM 输入场景**

提供 Rust 库与 CLI，将 DOCX/PPTX/XLSX/XLS/HTML/CSV/JSON/XML/Jupyter Notebook、代码文件、纯文本及多种图片格式转换为 Markdown（并输出直接提取的纯文本），格式由魔数与扩展名自动检测，PDF 明确排除。表格统一渲染为管道表格并处理合并单元格；可选通过 ImageDescriber trait 接入 LLM（内置 Gemini 实现）生成图片 alt 文本。支持编译到 WASM 在浏览器/边缘运行时使用，提供 npm 包。安装方式包括 cargo add/install 与 npm install。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 12 类格式转换，含 DOCX/PPTX 合并单元格表格、批注提取、嵌入式图片导出
- 纯 Rust 实现，零外部运行时、无 C 绑定、无子进程调用
- 可选 LLM 生成图片 alt 文本（ImageDescriber trait，内置 Gemini 实现，含异步并发）
- 可编译为 WASM 在浏览器/Cloudflare Workers/Deno Deploy 等边缘运行时运行

## 适用场景

- 在 Rust 应用中把 Office 文档转为 Markdown 供 LLM 处理，避免捆绑 Python 运行时
- 在浏览器或边缘运行时做客户端文档转换，文档不离开用户设备
- 通过 CLI 批量把 DOCX/PPTX/XLSX 等文件转为 Markdown

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: A pure Rust tool and library that converts various document formats into Markdown — designed for LLM consumption.

## 星数曲线

```mermaid
xychart-beta
    title "developer0hye/anytomd-rs 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-30"]
    y-axis "stars" 55 --> 59
    line [56, 57, 58, 58]
```

2026-10-18 56 → 2026-10-30 58（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `6fc002d5a275` · [字段定义](../../DATASET.md)*
