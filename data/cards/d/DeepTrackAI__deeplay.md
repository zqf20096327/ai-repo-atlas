# DeepTrackAI/deeplay

⭐ 28 · Jupyter Notebook · MIT · 推送 2026-10-28 · [GitHub](https://github.com/DeepTrackAI/deeplay) · [官网](https://deeptrackai.github.io/deeplay/) · 组织维护

**扩展 PyTorch 的模块化深度学习库，支持创建后修改网络组件**

基于 PyTorch 的 Python 深度学习库，定位为 PyTorch 的模块化超集：保持与 PyTorch 代码兼容的同时，引入可在创建后动态修改子模块属性的机制，并通过层级抽象（Application/Model/Component/Block/Layer）组织网络结构，配合样式注册表实现组件定制。训练流程使用 PyTorch Lightning 简化。安装方式为 pip install deeplay，自动安装 PyTorch 与 PyTorch Lightning 依赖；提供系列入门 notebook 与文档站点。由 DeepTrackAI 团队维护，获 ERC 与 Wallenberg 基金资助。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型组件创建后可动态修改属性
- 与 PyTorch 代码保持兼容的超集设计
- 层级抽象：Application→Model→Component→Block→Layer
- 利用 PyTorch Lightning 简化训练循环

## 适用场景

- 需要跨项目复用网络组件的深度学习开发者
- 在模型创建后调整架构属性而无需重写代码
- 配合 PyTorch Lightning 进行模型设计与训练

## 场景标签

 · 领域:深度学习框架

## 证据(README 行号)

> L16: Deeplay is a deep learning library in Python that extends PyTorch with additional functionalities focused on modula
> L29: Deeplay is designed as a superset of PyTorch, retaining compatibility with PyTorch code while introducing features 

## 星数曲线

```mermaid
xychart-beta
    title "DeepTrackAI/deeplay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `31ceda7435c6` · [字段定义](../../DATASET.md)*
