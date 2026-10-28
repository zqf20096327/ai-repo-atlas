# orca-gamedev/img2blockbench

⭐ 28 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/orca-gamedev/img2blockbench) · 组织维护

**将 Minecraft 风格参考图转换为 Blockbench 原生模型的编译器与基准**

把单张 Minecraft 风格参考图转换为 .bbmodel 原生模型的工具：提供三条路线（mesh 引导的 cuboid 重建、直接 cuboid+纹理推理、img2threejs 场景转换），由外部 agent 提供视觉推理，本仓库提供工作流、模型契约、确定性编译器与质量门（UV 密度、结构审计、多视角 IoU 度量）。不绑定特定 LLM API，Route 1 的 3D 生成器由用户自选（基准用 Trellis）。附带 agent skill 可安装到 Codex/Claude Code，以及 npm 运行的对比 demo。直接路线要求输入已是 Minecraft 风格的图。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三条转换路线输出统一的 .bbmodel、纹理、geo.json 与审计包
- 确定性编译器处理 UV 打包、纹理迁移、Bedrock 几何与可复现清单
- 质量门与几何/轮廓 IoU 基准（五动物测试集）
- 附带可安装到 Codex/Claude Code 的 agent skill

## 适用场景

- 把 Minecraft 风格的生物参考图做成可用的 Blockbench 模型
- 为 Minecraft 模组/资源包生成带骨骼与碰撞信息的生物几何
- 复现或评估 image-to-Blockbench 转换的质量指标

## 场景标签

 · 领域:游戏内容生成/3D 工具

## 证据(README 行号)

> L3: Turn one Minecraft-style reference image into a native Blockbench model using
> L241: The agent supplies the visual reasoning. This repository supplies its workflow,

## 星数曲线

```mermaid
xychart-beta
    title "orca-gamedev/img2blockbench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c3370b545c2a` · [字段定义](../../DATASET.md)*
