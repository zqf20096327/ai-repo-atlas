# SonderSaid/ComfyUI-Sonder-Editor

⭐ 24 · Python · GPL-3.0 · 推送 2026-10-14 · [GitHub](https://github.com/SonderSaid/ComfyUI-Sonder-Editor) · 个人维护

**ComfyUI 的时间线视频编辑器自定义节点，支持长视频迭代生成**

以 ComfyUI 自定义节点形式提供的多轨时间线编辑界面：在项目内导入素材，把视频、音频、提示词、参考帧和 Reference 排布到时间线上，选取区间后交给下游已连接的 ComfyUI 生成工作流，输出回传为项目素材供审阅与回放对比。自带 LTX 2.3、MiniMax H3、Wan、HunyuanVideo、CogVideoX 等模型模板（帧数/FPS/分辨率约束），并提供 Guides、Driver、Reference 等桥接节点。限制：本体不生成内容，能力取决于所连接的扩散模型与工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多轨时间线（视频/音频/提示词/参考帧/Reference 轨道）与选区→生成窗口机制
- Reference Library 管理角色、场景、服装与声音，并按轨道区间与 recipe 打包
- 内置 8 种模型模板（LTX 2.3、MiniMax H3、Wan 2.1/2.2、HunyuanVideo、CogVideoX 等）约束时间线参数
- 渲染队列与批量渲染，逐帧合成导出（长度受磁盘而非内存限制）

## 适用场景

- 在 ComfyUI 中以时间线方式迭代制作长视频
- 用同一项目复用角色/场景/声音等 Reference 保持一致性
- 分镜分块排队渲染并对比多个生成版本

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L5: Sonder Editor is a timeline-based video editor for ComfyUI, built for iterative
> L14: Generation stays in ComfyUI — send the selection through the connected graph, then review or place the result
> L88: Sonder generates nothing itself, so what a project can do depends on the model

## 星数曲线

```mermaid
xychart-beta
    title "SonderSaid/ComfyUI-Sonder-Editor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fbcfb77107a7` · [字段定义](../../DATASET.md)*
