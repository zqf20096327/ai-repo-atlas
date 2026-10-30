# loumalouomega/meshioplusplus

⭐ 16 · C++ · MIT · 推送 2026-10-29 · [GitHub](https://github.com/loumalouomega/meshioplusplus) · [官网](https://loumalouomega.github.io/meshioplusplus/) · 个人维护

**多格式非结构网格读写与转换库（C++ 核心、多语言绑定）**

以单一 C++ 核心承载格式注册表、操作层与网格后端，上覆 Python、C、Fortran、Julia、R、WebAssembly 等语言接口，并构建 CLI、浏览器查看器、Blender 插件、ParaView 插件、PhysicsNeMo 适配器与 MCP server。支持 70 余种 CAE/网格格式（Abaqus、ANSYS、Nastran、Gmsh、VTK 系列、XDMF、Exodus 等）的读取、写入与相互转换，含时序、命名区域、点/单元集合等数据。供仿真、CAE 与科学计算用户做网格与结果文件的互操作。厂商私有格式（如 .odb）通过 contrib/ 下运行于厂商环境的脚本导出可读序列。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 C++ 核心，Python/C/Fortran/Julia/R/WASM 多语言接口
- 70 余种 CAE 与网格格式的读写与相互转换
- 提供 CLI、浏览器查看器、Blender 插件、ParaView 插件与 MCP server
- Pipeline 报告（steps/warnings）与 V2 版本的 Merge/Interpolate/Partition 操作

## 适用场景

- 在不同仿真软件的网格与结果格式之间转换文件
- 在 Python/Julia/Fortran 等环境中统一读取 CAE 数据
- 通过 MCP server 让 agent 工具链访问网格数据（如 sets_data）

## 场景标签

 · 领域:科学计算/CAE 数据处理

## 证据(README 行号)

> L109:  meshio++ architecture: one C++ core holding the format registry, the operations layer and one of three mesh backe
> L111: One C++ core, six language surfaces, and the tools built on them; the architecture page is the map, with every box

## 星数曲线

```mermaid
xychart-beta
    title "loumalouomega/meshioplusplus 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26", "2026-10-30"]
    y-axis "stars" 10 --> 17
    line [11, 14, 15, 16]
```

2026-10-18 11 → 2026-10-30 16（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `8df8c3a09a1c` · [字段定义](../../DATASET.md)*
