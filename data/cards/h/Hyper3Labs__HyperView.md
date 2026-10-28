# Hyper3Labs/HyperView

⭐ 20 · Python · MIT · 推送 2026-10-09 · [GitHub](https://github.com/Hyper3Labs/HyperView) · [官网](https://hyper3labs.github.io/docs/hyperview/) · 组织维护

**嵌入空间几何分析工作台：图像数据集转为可交互工作区**

面向数据集策展与模型内省的交互式几何工作台：从 Hugging Face 数据集或本地文件夹读取图像，用内置或自定义 provider 计算嵌入，投影到欧氏、Poincaré/双曲与球面布局；散点与缩略图、标签、最近邻关联，支持聚类与离群选择。提供 Python API、CLI 与工作区扩展机制，可导出为静态只读 bundle（由 Cloudflare Workers 静态资源服务），并为编码 agent 提供 CLI 控制平面。通过 uv 安装。

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

- 欧氏/双曲/球面三种几何布局的嵌入投影
- 从 Hugging Face 数据集或本地文件夹摄取图像并计算嵌入
- 工作区可导出为静态只读 Space，无 Python 或容器部署
- 编码 agent 可通过 CLI 控制运行中的工作区

## 适用场景

- 检查嵌入空间中的类别坍缩与边界样本
- 图像数据集策展：选择聚类与离群样本
- 把准备好的工作区以静态站点形式分享浏览

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L74: - Ingests image data from Hugging Face datasets or local folders.
> L75: - Computes embeddings with built-in or custom providers.
> L79: - Gives coding agents a CLI control plane for the same workspace humans inspect.

## 星数曲线

```mermaid
xychart-beta
    title "Hyper3Labs/HyperView 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `97e61a46c0f8` · [字段定义](../../DATASET.md)*
