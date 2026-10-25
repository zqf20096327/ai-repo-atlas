# ysichov/ACE

⭐ 49 · ABAP · MIT · 推送 2026-10-09 · [GitHub](https://github.com/ysichov/ACE) · 个人维护

**SAP GUI 内的 ABAP 静态代码浏览与度量工具**

ACE 是运行于 SAP GUI for Windows 的 ABAP 静态分析工具：解析源代码而不执行被分析对象，提供调用流程视图（Code Flow）、静态调用映射、Mermaid 流程图（需可选的 abapMermaid）、反向程序切片式的数据依赖分析（追踪变量取值来源、跨调用解析参数改名）、McCabe/Halstead/可维护性度量及骨架视图。面向接手陌生系统的顾问、维护遗留代码的开发者与升级前做影响分析的评审人员。要求 SAP NetWeaver AS ABAP 7.50+ 与源代码读权限；经 abapGit 或单文件方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数据依赖分析（backward slicing）：选定变量后展示产生该值的全部语句链
- Code Flow 将多个 include/FORM/方法按执行顺序合成单一源视图
- McCabe/Halstead/Maintainability Index 度量与热点排序
- Only Z 模式仅跟踪客户代码（Z*/Y*//NAMESPACE/*），支持多窗口并行分析

## 适用场景

- 接手大型遗留 ABAP 报表时理解调用结构与取值来源
- 变更前做影响分析，查看整个程序或包的静态调用图
- 为同事或 LLM 生成对象的结构骨架说明
- 识别高复杂度的危险方法与热点

## 场景标签

 · 领域:软件开发工具/代码分析

## 证据(README 行号)

> L25: |"I need to explain this object to a colleague or an LLM"|Copy 3000 lines of source|Skeleton view — structure, call
> L214: This is the feature the tool was built for. In programming theory it is called **backward program

## 星数曲线

```mermaid
xychart-beta
    title "ysichov/ACE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-25 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `faf5bff933f5` · [字段定义](../../DATASET.md)*
