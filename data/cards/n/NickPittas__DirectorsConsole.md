# NickPittas/DirectorsConsole

⭐ 363 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/NickPittas/DirectorsConsole) · 个人维护

**面向电影人的 AI 图像/视频生成工作台：提示词设计+ComfyUI并行渲染**

三合一工作区：Cinema Prompt Engineering 提供基于规则的影视提示词生成与可选的 LLM 图像感知增强（支持 Google AI Gemini API key、Antigravity OAuth 及兼容本地服务器）；Storyboard 导入 ComfyUI 工作流，通过 REST/WebSocket 向一个或多个本地/远程 ComfyUI 节点并行提交渲染任务；Gallery 负责项目媒体的浏览、评分、标签与比较。面向电影制作者与 AI 艺术家。源码启动，需 Python 3.11+ 与 Node.js 22.13+；无应用级鉴权，仅限可信私有网络使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于规则的电影摄影提示词生成，可选用视觉 LLM 增强（文本/图像/混合输入）
- 通过 REST/WebSocket 并行驱动多个本地或远程 ComfyUI 渲染节点
- Gallery 项目媒体管理：过滤、比较、评分、标签、回收站恢复
- 三服务架构：前端 UI、CPE 后端、Orchestrator

## 适用场景

- 为分镜镜头设计电影感提示词并送 ComfyUI 渲染
- 同时向多个 ComfyUI 节点提交并行渲染任务并跟踪进度
- 在项目内统一管理、比较与整理生成的图像和视频

## 场景标签

`提示工程` `图像生成` `视频生成` · 领域:Agent 开发

## 证据(README 行号)

> L5: Director's Console brings cinematic prompt design, reference-driven image and video workflows, and project media man
> L28: **Generate** creates rule-based text from the current configuration. **Enhance with AI** sends the selected LLM the
> L38: Storyboard is the execution workspace. Import or select a ComfyUI workflow, expose its supported controls, assign p

## 星数曲线

```mermaid
xychart-beta
    title "NickPittas/DirectorsConsole 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-24"]
    y-axis "stars" 359 --> 364
    line [360, 361, 363, 363]
```

2026-10-18 360 → 2026-10-24 363（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `d146cbbe2754` · [字段定义](../../DATASET.md)*
