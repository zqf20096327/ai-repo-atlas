# adamandama/Strata-Model-Importer

⭐ 4 · Python · NOASSERTION · 推送 2026-11-04 · [GitHub](https://github.com/adamandama/Strata-Model-Importer) · 个人维护 · 中文 README

**Windows 用户一键把 GGUF 模型接入 Strata 推理引擎的 GUI 工具**

面向 Windows 用户的 Tkinter 图形化导入工具：把微调版、去限制版或社区量化 GGUF 接入 Strata 本地推理引擎，自动完成打包（调用 Strata 自带 tools/iq_pack.py）、分片识别与挂载、MTP 投机解码检测/编译/降级、配置生成与 run-*.bat 启动器生成。全程本地运行、零第三方依赖（仅 Python 标准库），另提供 importer.py 无头命令行模式用于批量导入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 GUI 一键导入，无需命令行与 JSON 手工编辑
- 分片识别：自动将第 2 分卷挂为 --ple-gguf，跳过 mmproj 等非模型文件
- MTP 投机解码自适应：复用/编译/无草稿头时安全剥离参数
- 每个模型独立 pack、配置与启动器，可多模型并存

## 适用场景

- 把第三方微调或量化 GGUF 模型接入 Strata 本地推理
- 同时管理多个本地模型并为每个生成独立启动器
- 避免手写 strata-*.json 与命令行参数配置

## 场景标签

 · 领域:本地 LLM 推理工具

## 证据(README 行号)

> L7: 把任何第三方微调 / 去限制（Abliterated）/ 社区量化 GGUF，一键接入 Strata 推理引擎。
> L69: |Strata|any install or source checkout containing `tools/iq_pack.py` + `tools/gguf_reader.py` (both ship with Strat

## 星数曲线

```mermaid
xychart-beta
    title "adamandama/Strata-Model-Importer 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-27"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-08 4 → 2026-11-27 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `a1a5f100df37` · [字段定义](../../DATASET.md)*
