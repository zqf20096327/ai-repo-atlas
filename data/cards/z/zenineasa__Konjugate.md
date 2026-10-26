# zenineasa/Konjugate

⭐ 32 · JavaScript · MPL-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/zenineasa/Konjugate) · [官网](https://konjugate.com) · 个人维护

**面向工程仿真与数字孪生的图原生可组合仿真引擎**

开源图原生仿真引擎：将物理系统表示为组件节点与关系边组成的网络，节点定义状态与属性，边定义控制量传输与变换的方程，从而由小的交互模型组合出复杂系统动力学。支持分段时变项、从多元时序 CSV 做两阶段因果推断自动提议起始图、FMU 导入/导出、数值稳定性诊断。以 Electron 桌面应用形式分发（macOS/Windows/Linux，另有浏览器预览），内置扩展发现与一键安装机制，已有物流、金融、机器人等插件。项目自述为公测阶段，应用未代码签名。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 图原生建模：节点为状态组件、边为交互方程，由可复用小模型组合系统
- 两阶段因果推断：滞后偏相关筛选 + 联合岭回归，从时序 CSV 提议模型图
- FMU 导入/导出与数值稳定性诊断
- 内置扩展发现器一键安装插件（物流/金融/机器人等）

## 适用场景

- 用可组合的组件网络为多物理耦合系统建模
- 从传感器时序数据推断变量间因果结构并生成起始模型
- 构建工程系统的数字孪生并做供应链/金融/机器人等领域仿真

## 场景标签

 · 领域:工程仿真/数字孪生

## 证据(README 行号)

> L5: The objective is to simplify the process of modelling complex physical systems by representing them as networks of i
> L85: Konjugate can propose a starting graph from that data directly. Import a CSV of multivariate timeseries, and it fin
> L119: Want a quick look before installing anything? A free, in-browser trial of Konjugate needs no install: **try it at 

## 星数曲线

```mermaid
xychart-beta
    title "zenineasa/Konjugate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6e89bfbbba88` · [字段定义](../../DATASET.md)*
