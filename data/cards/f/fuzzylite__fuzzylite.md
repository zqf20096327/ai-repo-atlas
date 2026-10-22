# fuzzylite/fuzzylite

⭐ 328 · C++ · GPL-3.0 · 推送 2026-10-03 · [GitHub](https://github.com/fuzzylite/fuzzylite) · [官网](https://fuzzylite.com) · 组织维护

**C++ 模糊逻辑控制库：设计并运行模糊控制器**

由 FuzzyLite Limited 维护的 C++ 模糊逻辑控制库，采用面向对象模型，对外部库依赖很少。提供 6 种控制器（Mamdani、Takagi-Sugeno 等）、25 种语言项、多种激活/T-Norm/S-Norm/去模糊化方法，支持 fll/fis/fcl 格式导入与 C++/Java/R 等 7 种格式导出，附 30+ 示例与交互式控制台。以源码 + CMake 构建方式提供，产出控制台程序、静态与动态库；双许可（GPLv3 或商业许可），另有付费 GUI 产品 QtFuzzyLite。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 种控制器类型与 25 种语言项、7 种去模糊化器
- fll/fis/fcl 导入，C++/Java/fll/fld/R/fis/fcl 导出
- CMake 源码构建，产出控制台程序与静态/动态库
- 交互式控制台可手动输入值评估控制器

## 适用场景

- 在 C++ 项目中嵌入模糊逻辑控制器（如避障、温控）
- 导入 Matlab/Octave 的 fis/fcl 模型并在本库中运行
- 跨语言导出控制器定义用于对比与基准测试

## 场景标签

 · 领域:控制系统/软计算

## 证据(README 行号)

> L3:  A Fuzzy Logic Control Library in C++
> L27: The **goal** of the FuzzyLite Libraries is to **easily** design and **efficiently** operate fuzzy logic controllers

## 星数曲线

```mermaid
xychart-beta
    title "fuzzylite/fuzzylite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 326 --> 328
    line [327, 327]
```

2026-10-18 327 → 2026-10-22 327（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `db90cd03603e` · [字段定义](../../DATASET.md)*
