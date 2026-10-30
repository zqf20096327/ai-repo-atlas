# januspluto/ComfyUI-Krea2-Regional

⭐ 16 · Python · MIT · 推送 2026-08-06 · [GitHub](https://github.com/januspluto/ComfyUI-Krea2-Regional) · 个人维护

**ComfyUI 的 Krea 2 区域提示与区域 LoRA 自定义节点包**

面向 ComfyUI 用户的自定义节点包，为 Krea 2 文生图模型提供单次前向（single-pass）的区域生成能力：在画布编辑器上绘制矩形/套索区域，为每个区域绑定独立提示词与 LoRA，通过联合注意力掩码和逐 token 门控的 LoRA delta 实现区域隔离，且不破坏 ComfyUI 自身的 LoRA 权重加载。附带可选的第二遍 Regional Detailer 修复身份串扰，支持 PEFT/kohya/LoKr 格式 LoRA。要求 ComfyUI v0.26+ 原生 Krea 2 支持，1.2.0 版在 0.29–0.30 测试。以 git clone 到 custom_nodes 目录方式安装，无额外 Python 依赖。

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

- 单次前向的区域生成：所有提示拼接为一条文本序列，联合注意力掩码隔离各区域
- 逐 token 门控的区域 LoRA，全局 LoRA 可叠加
- 画布编辑器：矩形/套索区域、可编辑顶点、区域列表兼作前后深度
- Regional Detailer 第二遍按主体轮廓修复身份串扰

## 适用场景

- 文生图中让不同角色/主体各占指定区域并携带各自 LoRA
- 多角色生成时控制风格与身份串扰
- 通过图像 captioner 自动从参考图生成区域布局

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Regional prompting and **per-region LoRA** for Krea 2
> L70: **Krea2 Apply Regional** — patches the model for single-pass regional
> L91: **Krea2 Regional LoRA** / **Krea2 Regional Prompt** — lower-level building

## 星数曲线

```mermaid
xychart-beta
    title "januspluto/ComfyUI-Krea2-Regional 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9f2863690ed0` · [字段定义](../../DATASET.md)*
