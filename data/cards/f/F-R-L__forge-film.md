# F-R-L/forge-film

⭐ 539 · Python · MIT · 推送 2026-03-26 · [GitHub](https://github.com/F-R-L/forge-film) · 个人维护 · 中文 README

**多模型并行 AI 影片生成引擎：故事编译为 DAG 按关键路径调度**

用户提交故事文本，Forge 用 LLM（GPT-4o/Claude/DeepSeek）将其编译为场景依赖 DAG，用关键路径法（CPM）调度多个 worker 并行生成：按场景类型把对白路由到 Kling、风景路由到本地 CogVideoX 等；跨模型场景间提取上一场景末帧并做直方图色彩匹配作为 i2v 种子保持连续性，最终 ffmpeg 单次拼接输出 final.mp4。支持 Kling/Seedance 云端 API 与 CogVideoX/Wan 本地后端，后端实现统一 BasePipeline 接口可插拔（约 50 行接入新模型）。提供 CLI、Gradio Web UI 与 Python 库三种使用方式；场景失败按指数退避重试。限制：Seedance 与 Wan 后端在 Roadmap 中标记未完成，真实基准测试未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 故事→DAG 编译 + CPM 关键路径并行调度，无依赖场景同时生成
- 按场景类型的多模型路由（forge.yaml 可配置）
- 跨模型连续性：末帧提取 + 直方图色彩匹配作为 i2v 种子
- 可插拔后端接口与 mock 后端（无需 API key 全流程测试）

## 适用场景

- 写一段故事自动生成多场景短片，免去多平台手工拼接
- 混合云端与本地视频模型降低成本并保持画面连续
- 复现或扩展 DAG 并行调度策略做影视生成实验

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L16: **Forge automates the entire pipeline.** You write a story. Forge compiles it into a scene graph, routes each scene
> L20: 🧭 **Story → DAG** — GPT-4o (or Claude / DeepSeek) compiles your story into a dependency graph. Scenes with no depen
> L26: 🎨 **Cross-model continuity** — when scene B (CogVideoX) follows scene A (Kling), Forge extracts A's last frame, app

## 星数曲线

```mermaid
xychart-beta
    title "F-R-L/forge-film 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 538 --> 541
    line [539, 540, 540]
```

2026-10-18 539 → 2026-10-22 540（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `6aef8cc4697d` · [字段定义](../../DATASET.md)*
