# curiosity-ai/umap-sharp

⭐ 51 · C# · MIT · 推送 2026-01-22 · [GitHub](https://github.com/curiosity-ai/umap-sharp) · 组织维护

**C# 实现的 UMAP 降维库：把高维向量投影到 2D/3D**

UMAP 算法的 C# 重实现（自 JavaScript 版转写，源自 Python 版），读取等长 float 向量数组，经 InitializeFit/Step/GetEmbedding 流程输出降维后的向量，可用于可视化或一般非线性降维。支持自定义距离函数（默认余弦）、维度数、邻居数、进度回调等配置；采用类似 fastText 的无锁多线程优化，可用固定种子随机生成器禁用并行以保证确定性。通过 NuGet 分发，附加载 MNIST 向量生成标签可视化图的示例控制台项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- UMAP 降维算法的 C# 实现（InitializeFit/Step/GetEmbedding 流程）
- 可配置维度、距离函数、邻居数与自定义随机数生成器
- 类似 fastText 的无锁多线程优化，可禁用并行
- 附带 MNIST 数据可视化示例项目

## 适用场景

- 把文档或实体的 embedding 向量降到 2-3 维以绘图探索聚类
- 在 .NET 项目中做非线性降维而无需调用 Python 环境
- 结合标签生成 2D/3D 可视化图

## 场景标签

 · 领域:机器学习库/降维可视化

## 证据(README 行号)

> L7: "Uniform Manifold Approximation and Projection (UMAP) is a dimension reduction technique that can be used for visual
> L21: Instantiate a **Umap** instance, pass the array of vectors to the "InitializeFit" method, receive a recommended num

## 星数曲线

```mermaid
xychart-beta
    title "curiosity-ai/umap-sharp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-24 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4c062cbe1e32` · [字段定义](../../DATASET.md)*
