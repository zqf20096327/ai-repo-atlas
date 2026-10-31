# robertZaufall/mindmanager_ai

⭐ 70 · Python · MIT · 推送 2026-02-07 · [GitHub](https://github.com/robertZaufall/mindmanager_ai) · 个人维护

**给 MindManager 用户的 AI 思维导图增强宏与脚本集**

面向 MindManager（Windows/macOS）思维导图用户的自动化宏与 Python 脚本集合：通过原生 API 请求接入 20 余家 LLM 平台（含 Azure OpenAI、OpenAI、Anthropic、Ollama 等本地运行时）以及图像/视频生成与 DeepL 翻译服务，对导图或选中主题执行精炼、聚类、生成示例、PDF 转导图、导出 Mermaid/Markmap HTML 等操作。提供 Tkinter 图形界面与 Agent 标签页（Agno/Autogen/CrewAI 示例）。Windows 侧需 Chocolatey 安装 Python 并注册宏，macOS 侧需 Python 与 Automator 工作流；本地模型需 Apple Silicon 或 8GB 显存以上 NVIDIA 卡。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接入 20+ LLM 提供商（含 Ollama/GPT4All/LMStudio/MLX 本地运行时）
- 图像生成（Flux/DALL-E/SD 等）与视频生成（Sora/Veo）
- PDF 批量转思维导图，含 markdown 转换与内容清洗
- Tkinter 界面：操作、图像、自由文本、翻译、Agent、配置六个标签页

## 适用场景

- 对现有思维导图做 AI 精炼、聚类与示例生成
- 把 PDF 文档转成思维导图
- 基于导图主题生成配图并插入 MindManager 图库
- 用 DeepL 翻译整个导图的主题

## 场景标签

`图像生成` `视频生成` `文档解析` · 领域:内容生成

## 证据(README 行号)

> L3: These automations and macros enhance mindmaps created by **MindManager** on macOS and Windows.
> L62: - Windows compatible (run macro/context menu or call the **Python** script directly)
> L63: - macOS compatible (run **Automator** workflow (Quick Action) or call the **Python** script directly)

## 星数曲线

```mermaid
xychart-beta
    title "robertZaufall/mindmanager_ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-31 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2b7857c9915e` · [字段定义](../../DATASET.md)*
