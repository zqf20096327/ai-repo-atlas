# ai-screams/HwpForge

⭐ 20 · Rust · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/ai-screams/HwpForge) · [官网](https://ai-scream.ai/HwpForge/) · 组织维护

**Rust 库：编程读写/转换韩文 HWP/HWPX 文档，含 MCP 服务器**

纯 Rust 库，读写与转换韩文 Hancom HWPX（ZIP+XML，KS X 6101）及旧版 HWP5 文档。提供 Markdown↔HWPX 双向转换、JSON round-trip 编辑、YAML 样式模板与 PDF 导出（依赖排版缓存）。三种入口：CLI 工具 Hammer、MCP 服务器 Vise（19 个工具，供 Claude Code/Codex/Cursor 等 AI 工具直接生成编辑韩文文档）、Python 绑定（abi3 wheel，零运行时依赖）。限制：MCP surface 处于 Beta，CLI 构建 CLI 需 Rust 1.92+，PDF 仅能渲染含排版缓存的文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Markdown↔HWPX 双向转换与 JSON round-trip 编辑
- MCP 服务器提供 19 个文档操作工具，兼容多种 MCP 宿主
- HWPX 无损解码/编码，HWP5 读取与转换
- Python abi3 wheel 零运行时依赖，覆盖 Linux/macOS/Windows

## 适用场景

- 让 Claude 等 AI 工具直接生成和编辑韩文 HWPX 公文
- 把已有韩文文档转成 Markdown 供 LLM 读取分析
- 在 Rust/Python 程序中程序化生成与批量处理韩文文档

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L123: Claude Code, Codex CLI, Claude, ChatGPT, Cursor, Antigravity 등 MCP 지원 AI 도구에서 **한글 문서를 직접 생성하고 편집할** 수 있습니다. 현재 MC
> L240: > **왜 MCP?** CLI(Hammer)는 AI가 `bash` 명령을 실행해야 하지만, MCP(Vise)는 AI가 **네이티브 도구로**
> L50: **LLM-first 설계** 🔥 — AI 친화적인 Markdown과 공식 한글 문서 포맷(HWPX), 두 세계를 자연스럽게 잇습니다. LLM이 Markdown으로 작성한 내용은 공문서 규격의 HWPX로 컴

## 星数曲线

```mermaid
xychart-beta
    title "ai-screams/HwpForge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2107fb10def0` · [字段定义](../../DATASET.md)*
