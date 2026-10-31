# Renumics/mesh2vec

⭐ 17 · KFramework · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Renumics/mesh2vec) · 组织维护

**将 LS-DYNA CAE 网格数据转为等长单元特征向量供机器学习使用**

Python 库，读取 LS-DYNA 的 CAE 网格数据（经由 ANSA 接口），计算单元及其邻域的质量度量（如 aspect、warpage），按层级聚合成等长特征向量，输出 DataFrame 作为机器学习方法的输入，并可用 Plotly 可视化单个聚合特征在网格上的分布。作者称这是传统网格与图方法用于自动网格质量分析的替代路径。pip 安装，部分功能依赖环境变量指向的 ANSA 可执行程序，属商业前处理软件依赖。

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

- 从 ANSA 壳网格文件加载网格并添加单元质量特征
- 按邻域层级（如 [0,2,3]）用聚合函数生成等长特征向量
- to_dataframe 输出特征向量，get_visualization_plotly 可视化

## 适用场景

- 为 CAE 网格质量预测模型准备特征输入
- 对 LS-DYNA 仿真网格做特征提取与可视化检查

## 场景标签

 · 领域:工程仿真/CAE 机器学习

## 证据(README 行号)

> L13: It utilizes various quality metrics of elements and their surrounding neighborhood to aggregate feature vectors for

## 星数曲线

```mermaid
xychart-beta
    title "Renumics/mesh2vec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `6b2a615e663c` · [字段定义](../../DATASET.md)*
