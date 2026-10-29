# Mechse/saft

⭐ 20 · Odin · 推送 2026-06-02 · [GitHub](https://github.com/Mechse/saft) · 个人维护

**用 Apple 本地大模型生成 Git 提交信息的命令行工具**

macOS 上的命令行工具，调用 Apple 设备端语言模型读取暂存区变更并生成 Git 提交信息。无需 API key，不联网，数据不出本机。通过 curl 安装脚本安装到 /usr/local/bin，提供卸载命令；README 另建议审计脚本内容后再执行。仅面向 Apple 平台，含 Roadmap 未列细节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用 Apple 设备端语言模型生成提交信息
- 无需 API key、不联网、数据不出本机
- 提供安装脚本与卸载命令，支持先审计脚本

## 适用场景

- 在 Mac 上自动生成 Git 提交信息
- 不愿使用云端 API 的本地提交信息生成

## 场景标签

`代码生成` `AI 写作` · 领域:编码与开发

## 证据(README 行号)

> L3: A Git commit-message generator powered by Apple's on-device language model.
> L4: No API keys. No cloud. No data leaves your Mac.

## 星数曲线

```mermaid
xychart-beta
    title "Mechse/saft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1b7a521c7a55` · [字段定义](../../DATASET.md)*
