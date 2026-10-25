# CUTEPKQ/NEWTON

⭐ 139 · Python · MIT · 推送 2026-07-31 · [GitHub](https://github.com/CUTEPKQ/NEWTON) · [官网](https://newton026.github.io/newton/) · 组织维护

**科研用 agent 规划框架：让视频生成满足物理常识**

论文配套项目（arXiv 可引）。将视频生成降级为 agent 工具箱中的一个动作：可训练的 Planner LLM 调用 Genesis 物理仿真、关键帧生成、图像生成/搜索、提示词精炼等工具构建物理条件，Gemini 盲测 A/B 作为 Verifier 闭环迭代重规划。推理时以 Planner→Executer→Verifier 多轮循环运行，每轮输出视频、仿真参考与完整 trace.json。依赖外部 API（OpenAI 兼容 LLM、Gemini、Seedance、Serper），需配置 API key，训练代码尚未发布（Roadmap 未勾选）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Planner→Executer→Verifier 多轮循环，视频生成仅是工具之一
- simulate 工具基于 Genesis 生成物理正确的参考视频与物体轨迹
- Planner 是唯一可训练组件，经 Flow-GRPO 在多轮循环中在线优化
- 提供 Claude Code slash 命令（/setup、/run）自动完成环境配置与运行

## 适用场景

- 在物理场景描述下生成符合物理常识的视频
- 复现论文中 VideoPhy-2 的 agentic 规划实验
- 研究以验证器闭环做多轮重规划的 agent 框架

## 场景标签

`Agent 框架` `视频生成` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L29: We present **Newton**, in which video generation is demoted from the system
> L34: on-policy via Flow-GRPO inside the live multi-turn loop. On VideoPhy-2, Newton
> L128: python loop/run_loop.py "a moving billiard ball rolls across a table and strikes a stationary ball head-on, transf

## 星数曲线

```mermaid
xychart-beta
    title "CUTEPKQ/NEWTON 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 138 --> 140
    line [139, 139]
```

2026-10-18 139 → 2026-10-25 139（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `a381cd364aef` · [字段定义](../../DATASET.md)*
