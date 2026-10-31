# Kiwi-shijie/ComfyUI_MiniMaxH3_Smart_Director

⭐ 21 · Python · MIT · 推送 2026-08-27 · [GitHub](https://github.com/Kiwi-shijie/ComfyUI_MiniMaxH3_Smart_Director) · 个人维护 · 中文 README

**ComfyUI 中文节点：MiniMax H3 视频分镜规划与一体化生成**

面向 ComfyUI 用户的中文一体化智能导演节点：输入一句主题、普通剧本或结构化分镜 JSON，自动判断 t2v/i2v/fl2v/r2v 生成模式，编译 MMX_DIR_GROUP 并在节点内部调用 AIMixer MiniMaxH3Director，直接输出视频帧、音频和运行报告。支持长视频 5/10/15 秒分段接力与自动拼接、可选本地 LLM（GGUF）或 OpenAI 兼容 API 做提示词优化、可选二采/放大。依赖 AIMixer/ComfyUI_MiniMaxH3_Director，本地 LLM 优化为可选功能需另装 ComfyUI-llama_Reversal。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动判断 t2v/i2v/fl2v/r2v 并生成 MMX_DIR_GROUP 一体化执行
- 长视频按 5/10/15 秒分段接力，Motion Context 承接上一段尾帧并自动拼接
- 提示词优化支持关闭/本地 LLM（GGUF）/OpenAI 兼容 API 三种模式
- R2V 长视频时间轴防循环策略：参考视频/音频按整片时间轴切片

## 适用场景

- 用中文剧本或一句主题直接在 ComfyUI 生成多镜头视频
- 把长片拆成多段接力生成并自动拼接为单个视频
- 用参考图片/视频/音频做主体一致性生成

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L9: 主节点是 `MiniMax H3 智能导演 一体化`：它会自动编译分镜、判断 `t2v/i2v/fl2v/r2v`、生成
> L22: - 一体化执行：主节点自己接 `model / video_vae / audio_vae / clip` 和采样参数，内部调用 AIMixer Director，不需要再摆一个 Director 节点。
> L67: 依赖项目：AIMixer/ComfyUI_MiniMaxH3_Director。本地 LLM 优化为可选功能，使用时再安装 `ComfyUI-llama_Reversal`。

## 星数曲线

```mermaid
xychart-beta
    title "Kiwi-shijie/ComfyUI_MiniMaxH3_Smart_Director 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4128917eceb3` · [字段定义](../../DATASET.md)*
