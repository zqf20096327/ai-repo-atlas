# connorkapoor/Palmetto

⭐ 29 · C++ · MIT · 推送 2026-01-19 · [GitHub](https://github.com/connorkapoor/Palmetto) · [官网](https://palmettocad.com) · 个人维护

**面向制造服务的 CAD 特征识别与 DFM 检查 Web 工作台**

基于 Web 的 CAD 可制造性（DFM）分析与特征检查工具：C++ 引擎基于 OpenCASCADE 与 Analysis Situs 框架构建属性邻接图（AAG），识别孔、型腔、圆角、倒角等特征，并对注塑、CNC、3D 打印、钣金、熔模铸造 5 种工艺做规则检查（壁厚、拔模角、底切、刀具可达性等）。FastAPI 后端加 React/Three.js 前端提供 STEP 上传、3D 可视化与 glTF 渲染；自然语言几何查询通过 Anthropic SDK 调用 Claude API 实现。使用前需分别编译 C++ 引擎、配置后端与前端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AAG 图表示上的 C++ 特征识别（孔/型腔/圆角/倒角/混合面）
- 覆盖 5 种制造工艺的 DFM 规则检查
- 体积化壁厚分析（SDF）与基于 Intel Embree 的射线底切检测
- Claude API 自然语言几何查询与 Three.js 面级高亮可视化

## 适用场景

- 上传 STEP 模型做注塑/CNC 等工艺的可制造性检查
- 自动识别 CAD 模型中的孔、型腔、圆角等制造特征
- 用自然语言查询几何（如查找大于 10mm 的孔）

## 场景标签

 · 领域:CAD/制造工程

## 证据(README 行号)

> L12: Palmetto is an expandable DFM (Design for Manufacturing) and feature checking tool that uses graph-based feature re
> L19: - **Natural Language Interface**: Powered by Claude API for intuitive feature queries
> L21: - **DFM Analysis**: Comprehensive manufacturability checks for 5 manufacturing processes

## 星数曲线

```mermaid
xychart-beta
    title "connorkapoor/Palmetto 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-31 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0e951e86afe2` · [字段定义](../../DATASET.md)*
