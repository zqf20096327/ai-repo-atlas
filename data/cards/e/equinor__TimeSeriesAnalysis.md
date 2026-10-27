# equinor/TimeSeriesAnalysis

⭐ 23 · C# · Apache-2.0 · 推送 2026-09-30 · [GitHub](https://github.com/equinor/TimeSeriesAnalysis) · [官网](https://equinor.github.io/TimeSeriesAnalysis) · 组织维护

**工业过程时间序列的系统辨识与动态仿真 .NET 库**

Equinor 维护的 C#/.NET 库，从工业过程的时间序列数据出发，基于系统辨识方法（多步修正线性回归）识别动态单元模型，可将单元模型串联成含 PID 反馈回路的互联网络进行仿真。模型参数少、保持可解释，支持灰箱建模，用途包括数字孪生、异常检测、what-if 场景评估与 PID 整定。目标框架 .NET Standard 2.0，可被 C#、Python（Python.NET 绑定）、Matlab 调用，示例以 NUnit 单元测试形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从时间序列数据辨识动态单元模型，支持链式互联与 PID 反馈回路仿真
- 低参数量设计，模型可解释并支持灰箱建模
- 可从 C#、Python、Matlab 引用（.NET Standard 2.0）
- 示例以 NUnit 单元测试形式实现

## 适用场景

- 为工厂过程环节构建数字孪生模型
- 通过实测值与模型值的偏差做异常检测与过程监控
- 仿真 what-if 场景评估 PID 控制器重新整定的收益
- 批量构建同类单元（阀门、分离罐、PID 回路）模型用于监控筛选

## 场景标签

 · 领域:工业过程建模/控制

## 证据(README 行号)

> L16: Models are not derived from physical first principles, but are inferred from time-series data using the principles 
> L34: Note that although this library uses regression methods and algorithms to learn parameters to describe data, the me

## 星数曲线

```mermaid
xychart-beta
    title "equinor/TimeSeriesAnalysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `5f18bdadcbad` · [字段定义](../../DATASET.md)*
