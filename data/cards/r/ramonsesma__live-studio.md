# ramonsesma/live-studio

⭐ 16 · TypeScript · NOASSERTION · 推送 2026-07-09 · [GitHub](https://github.com/ramonsesma/live-studio) · 个人维护

**Ableton Live 模块化超级扩展：144 模块 414 工具加 AI 副驾**

把数十个音乐制作扩展合并为一个 Ableton Live 扩展：单一本地服务器 + 单一 webview 承载 144 个模块、414 个工具、90 个快捷操作与 ⌘K 命令面板，面板懒加载。内置 AI copilot（OpenRouter/OpenAI/Gemini/NVIDIA NIM/OpenCode Zen，tool-calling 循环经 find_tools/run_tool 调用任意工具），提供计划模式（只读探索、逐步可撤销）、119 个富面板、项目仪表盘与每 1.5 秒的 SSE 实时刷新。普通用户安装 .ablx 包即可使用，开发者需 Node ≥ 22.11 与 Ableton Extensions SDK 从源码构建。适配 Live 12.4.5b+ beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 144 模块 414 工具合并为单一扩展与单一 webview，面板懒加载
- AI copilot 通过 tool-calling 元工具链调用全部 414 个工具
- ⌘K 命令面板索引全部工具与 90 个快捷操作
- Resonance Mix Radar：整集渲染→FFT 分析→掩蔽碰撞矩阵→一键修正

## 适用场景

- 在 Ableton Live 内用一个扩展替代多个分散扩展，避免端口冲突
- 用自然语言让 AI copilot 执行建轨、生成和弦与鼓组等操作
- 通过命令面板用键盘快速搜索执行任意工具

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L6:  144 modules · 414 tools · 90 quick actions · AI copilot · <code>⌘K</code> palette — all inside a single tabbed webv
> L26: - an **AI copilot** that drives any module via natural language,
> L34: - **AI copilot** (OpenRouter / OpenAI / Gemini / NVIDIA NIM / OpenCode Zen) with a *tool-calling* loop: it discover

## 星数曲线

```mermaid
xychart-beta
    title "ramonsesma/live-studio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fb321dad4395` · [字段定义](../../DATASET.md)*
