# obsfx/promptscout

⭐ 36 · TypeScript · MIT · 推送 2026-02-20 · [GitHub](https://github.com/obsfx/promptscout) · 个人维护

**用本地 LLM 为编码 agent 提示词附加代码库上下文的 CLI**

面向使用 Claude Code 等编码 agent 的开发者的 Node.js CLI 工具：本地运行 Qwen 3 4B（GGUF Q4_K_M，经 node-llama-cpp，约 2.5GB），根据提示词调用 5 个内置搜索工具（file_finder、section_finder、definition_finder、import_tracer、git_history），通过 ripgrep 和 git 在代码库中检索，将相关文件路径、代码片段与提交历史追加到原提示词后，结果复制到剪贴板。附带 Claude Code 插件，通过 UserPromptSubmit 钩子自动注入上下文，失败时静默回退。支持按目录的提示词模板。需要 Node.js >= 20、C++ 编译器、ripgrep、git 与约 3GB 磁盘空间。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 Qwen 3 4B（Q4_K_M）经 node-llama-cpp 运行，无需 API key 与云端
- 5 个基于 ripgrep/git 的搜索工具，由 LLM 决定调用与关键词
- Claude Code 插件经 UserPromptSubmit 钩子自动注入上下文，失败静默回退
- 按目录的提示词模板，nearest-ancestor 匹配，存于本地数据库

## 适用场景

- 给 Claude Code/Cursor/Copilot 提交提示词前自动附上相关代码上下文
- 减少编码 agent 自行探索代码库的 token 与时间消耗
- 在不同项目目录复用自定义提示词模板

## 场景标签

`提示工程` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L3: A CLI tool that enriches your coding agent prompts with codebase context using a local LLM. No API keys, no cloud. R
> L13: promptscout does that discovery locally, for free. A small local LLM reads your prompt, searches your codebase with
> L86: Once installed, every prompt you submit in Claude Code gets enriched with codebase context via the `UserPromptSubmi

## 星数曲线

```mermaid
xychart-beta
    title "obsfx/promptscout 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b663af4f95a2` · [字段定义](../../DATASET.md)*
