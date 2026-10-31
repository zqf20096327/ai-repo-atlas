# audeering/audformat

⭐ 13 · Python · NOASSERTION · 推送 2026-10-09 · [GitHub](https://github.com/audeering/audformat) · [官网](https://audeering.github.io/audformat/) · 组织维护

**媒体文件与标注的存储格式规范及 Python 参考实现**

audformat 定义音频、视频、文本等媒体数据与对应标注的统一存储格式：数据库为一个文件夹，包含媒体文件、YAML 头文件和一个或多个标注文件。以 Python 库形式提供参考实现，通过 audformat.Database 对象的 load()/save() 方法读写，便于机器学习项目中组合或替换数据库。由 audeering 团队以 MIT 许可维护，提供安装与格式规范文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 音频/视频/文本与标注的预定义存储格式规范
- audformat.Database 对象支持 load()/save() 读写
- MIT 许可的 Python 参考实现

## 适用场景

- 为机器学习项目统一组织媒体数据与标注
- 在不同数据库之间组合或替换数据集
- 按格式规范创建可交换的标注数据库

## 场景标签

 · 领域:多媒体/机器学习数据管理

## 证据(README 行号)

> L5: Specification and reference implementation of **audformat**.
> L11: This makes it easy to combine or replace databases

## 星数曲线

```mermaid
xychart-beta
    title "audeering/audformat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b396646d3412` · [字段定义](../../DATASET.md)*
