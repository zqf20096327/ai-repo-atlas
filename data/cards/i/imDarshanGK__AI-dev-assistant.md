# imDarshanGK/AI-dev-assistant

⭐ 83 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/imDarshanGK/AI-dev-assistant) · [官网](https://qyverixai.onrender.com/app) · 个人维护

**开源代码分析工作台：检测 bug、解释代码并给出改进建议**

基于 FastAPI 的 Web 代码分析平台：粘贴代码或上传 ZIP 项目，返回语言检测、纯英文解释、复杂度估计、45+ 种 bug 模式检查（Python/JavaScript/TypeScript/Java/C++ 专用，Python 另有 AST 深度分析）、0-100 质量评分与修改 diff。核心引擎为规则驱动（qyverix-engine-v3），可完全离线运行、无需账号与 API key；可选接入 OpenAI/Groq/Ollama 等 LLM 升级 /chat 问答。另含 WebSocket 实时多人协作、匿名/账号历史、分享链接、GitHub Action PR 机器人与 VS Code 扩展。运行需 Python 3.11/3.12 与 Node.js v18+，本地源码启动，无桌面安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 45+ 种 bug 模式检查覆盖 5 种语言，Python 含 AST 深度分析
- 规则引擎驱动，无 API key 可完全离线运行，可选切换 LLM
- ZIP 项目级分析、SSE 流式输出与 0-100 评分/前后 diff 视图
- WebSocket 实时多人协作、GitHub Action PR 分析与 VS Code 扩展

## 适用场景

- 粘贴或上传项目快速获得 bug 检测与改进建议
- 在 PR 中自动分析变更文件并评论结果
- 无 API key 环境下用规则引擎做离线代码审查
- 多人实时协作阅读与评注同一段代码

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L44: No account required for the core analysis. No API key needed. Works fully offline. Fully open source. An optional a
> L60: |**AI Chat Assistant**|Ask follow-up questions about your code at `/chat` - uses your configured LLM if enabled, ot
> L139: The app can still run without external AI providers when `LLM_ENABLED=false`. Accounts, history, favorites, and li

## 星数曲线

```mermaid
xychart-beta
    title "imDarshanGK/AI-dev-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 82 --> 84
    line [83, 83]
```

2026-10-18 83 → 2026-10-26 83（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `0cd5b4cf21db` · [字段定义](../../DATASET.md)*
