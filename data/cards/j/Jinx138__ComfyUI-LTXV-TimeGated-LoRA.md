# Jinx138/ComfyUI-LTXV-TimeGated-LoRA

⭐ 22 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/Jinx138/ComfyUI-LTXV-TimeGated-LoRA) · 个人维护

**ComfyUI 节点包：在 LTX 2.3 视频时间线上按段落调控 LoRA**

面向 ComfyUI 用户的 LTX 2.3 视频生成自定义节点包，提供 Temporal Director 共享时间线（最多 4 个语义段落，每段路由不同 prompt 并分配 LoRA）与独立 Time-Gated LoRA 节点两种方式。LoRA 强度曲线可用 q_in/q_out 及 shift 参数控制进出形状，支持运行时打补丁而不改写 LoRA 文件；附带调度预览节点与 sigma 裁剪工具。仅针对视觉 LoRA 层，不含音频门控；Scheduled Prompt Relay 依赖 ComfyUI-PromptRelay。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 共享时间线：最多 4 段落，各段独立 prompt 与 LoRA 分配
- q 曲线与 shift 参数控制 LoRA 进出形状与过渡偏移
- 运行时补丁方式应用 LoRA，无需改写 LoRA 文件
- 秒/帧双单位的调度预览节点与 sigma tail/trim 工具

## 适用场景

- 在 LTX 2.3 文生视频中让不同 LoRA 效果只出现在指定时间段
- 将 LoRA 过渡与 prompt 分段切换对齐或错开
- 在采样前检查完整的时间调度方案

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L11: ComfyUI-LTXV-TimeGated-LoRA provides two ways to control LoRAs over time:
> L71: |**LTXV Time-Gated LoRA (LTX 2.3)**|Standalone classic TimeGate workflow|

## 星数曲线

```mermaid
xychart-beta
    title "Jinx138/ComfyUI-LTXV-TimeGated-LoRA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7f10a2c8507e` · [字段定义](../../DATASET.md)*
