# AmyangXYZ/PoPo

⭐ 281 · TypeScript · GPL-3.0 · 推送 2026-02-10 · [GitHub](https://github.com/AmyangXYZ/PoPo) · [官网](https://popo-topaz-five.vercel.app) · 个人维护

**用自然语言生成 MMD 角色姿势与动画的 Web 应用**

面向 MMD（MikuMikuDance）创作者的 Web 应用：用户输入自然语言描述，经微调的 LLM 生成 MPL（MMD Pose Language）语义姿势代码，再映射为 MMD 骨骼动画并实时渲染。MPL 以结构化人类可读描述替代原始四元数，内置骨骼约束以避免解剖学上不可能的动作，生成的代码可读可改。技术栈为 Next.js/TypeScript 前端与 Reze Engine 渲染引擎，模型使用 GPT-4o-mini，部署于 Vercel，提供在线演示。README 未给出本地安装运行步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言→MPL 姿势代码→MMD 骨骼动画的生成管线
- MPL 语义姿势语言，生成结果可读可改
- 内置 MMD 骨骼约束与物理，适配动漫角色
- 基于 GPT-4o-mini 微调生成 MPL 代码

## 适用场景

- 想摆特定姿势但手动调骨骼困难的 MMD 创作者
- 快速生成并预览角色姿势与动画
- 通过阅读和修改生成的 MPL 代码微调姿势

## 场景标签

 · 领域:3D 动画/虚拟角色创作

## 证据(README 行号)

> L5: **PoPo** uses LLMs to generate MMD character poses from natural language descriptions. Instead of raw rotation quate
> L36: - **AI Model**: GPT-4o-mini for natural language → MPL generation

## 星数曲线

```mermaid
xychart-beta
    title "AmyangXYZ/PoPo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 279 --> 282
    line [280, 281, 281]
```

2026-10-18 280 → 2026-10-23 281（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9a655d6c7c07` · [字段定义](../../DATASET.md)*
