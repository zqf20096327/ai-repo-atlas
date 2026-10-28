# splunk/splunk-3D-graph-network-topology-viz

⭐ 28 · JavaScript · 推送 2026-05-27 · [GitHub](https://github.com/splunk/splunk-3D-graph-network-topology-viz) · [官网](https://splunkbase.splunk.com/app/4611/) · 组织维护

**面向 Splunk 的三维力导向图网络拓扑可视化应用**

Splunk 平台的自定义可视化应用，基于 ThreeJS/WebGL 以力导向图绘制对象间关系（如网络拓扑 src-dest 关系）。通过 SPL 查询输出 src/dest 字段即可生成 3D 图，支持节点/边的颜色与权重自定义、dashboard 下钻 token、lookup 表丰富样式。附带四个基于 NetworkX 的图算法示例 dashboard，需额外安装 Splunk MLTK 与 Python for Scientific Computing 库（仅示例需要）。通过 GitHub 或 Splunkbase 下载，安装在 Search Head 层，Apache 2.0 许可，由 Splunk 官方组织维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ThreeJS/WebGL 三维力导向图渲染 src-dest 关系数据
- 节点/边颜色与权重的可选字段自定义（lookup 表或 SPL eval）
- 支持 dashboard drilldown 点击节点回填 token
- 附带四个 NetworkX 图算法示例 dashboard

## 适用场景

- 在 Splunk dashboard 中以 3D 图查看网络通信或对象间拓扑关系
- 通过节点着色与权重量化展示关系强度
- 结合 MLTK 学习图分析算法在安全/网络数据上的应用

## 场景标签

 · 领域:数据可视化/网络安全分析

## 证据(README 行号)

> L8: Plot relationships between objects with force directed graph based on ThreeJS/WebGL.
> L75: Four dashboards are provided to show graph algorithms in action using NetworkX. Select them by clicking on `Graph E
> L79: * Splunk's Machine Learning Toolkit (MLTK)

## 星数曲线

```mermaid
xychart-beta
    title "splunk/splunk-3D-graph-network-topology-viz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `3edfdea41455` · [字段定义](../../DATASET.md)*
