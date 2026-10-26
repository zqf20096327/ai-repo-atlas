# phodal/coca

⭐ 991 · Go · MPL-2.0 · 推送 2026-01-06 · [GitHub](https://github.com/phodal/coca) · [官网](https://coca.migration.ink/) · 个人维护 · 中文 README

**遗留系统重构与分析工具箱：调用图、坏味道、依赖与 Git 分析**

用 Go 编写的命令行工具箱，面向遗留系统的重构、迁移与分析：生成调用图与反向调用图、扫描 Spring 注解 API、识别代码坏味道与测试坏味道、行数统计、模块化分析、Git 提交分析、概念分析、查找未使用依赖，并支持 rename/move/删除无用代码等自动化重构与设计模式建议。语言支持以 Java 为主（全特性）。提供 OSX/Linux/Windows 预编译二进制，也可 go install 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用图与反向调用图生成（dot 格式，需 graphviz）
- 代码坏味道与测试坏味道识别
- Git 提交分析与未使用依赖查找
- rename/move/清理无用代码的自动化重构

## 适用场景

- 分析遗留 Java 项目的调用与依赖结构
- 识别代码与测试中的坏味道以制定重构计划
- 统计模块行数与复杂度评估架构现状

## 场景标签

 · 领域:软件工程/代码分析

## 证据(README 行号)

> L8: > Coca is a toolbox which is design for legacy system refactoring and analysis, includes call graph, concept analysi
> L300: coca suggest

## 星数曲线

```mermaid
xychart-beta
    title "phodal/coca 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 990 --> 992
    line [991, 991]
```

2026-10-18 991 → 2026-10-26 991（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 low · 依据 README sha `d251d0078b60` · [字段定义](../../DATASET.md)*
