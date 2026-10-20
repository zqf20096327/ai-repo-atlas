# fboerncke/private-prompts-prototype

⭐ 38 · TypeScript · AGPL-3.0 · 推送 2025-10-29 · [GitHub](https://github.com/fboerncke/private-prompts-prototype) · [官网](https://www.privateprompts.org) · 个人维护

**本地桌面端 AI 提示词管理器：发送前自动假名化敏感数据**

面向注重隐私的个人用户的桌面应用（Windows/Linux/macOS 提供预构建安装包），核心功能是集中管理、编辑、打标签 AI 提示词，并在发送给外部 AI 服务前将用户定义的敏感信息（如姓名、邮箱）自动替换为占位符，收到回复后再自动还原。可选集成外部 AI 服务（当前仅 OpenAI）。附带全局历史与撤销、多语言、JSON 导入导出、明暗主题。限制：配置以未加密 JSON 明文存储；假名化不保证绝对匿名，上下文线索仍可能再识别；浏览器/扩展形态不建议生产使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 下载:GitHub Release 附件 累计 7,754(6 个 release)

## 能力要点

- 提示词发送前按用户规则自动假名化（敏感信息替换为占位符），回复后自动还原
- 数据仅存本地，刻意设计为桌面应用，不计划开发网页版
- 预构建二进制支持 Windows/Linux/macOS，含多语言与 JSON 导入导出
- 内置冲突检测机制处理替换规则与原文的冲突

## 适用场景

- 用 AI 写简历、求职信等含个人信息的文本时避免泄露隐私
- 集中管理和复用自己的提示词库
- 对外部 AI 服务发送提示词前对敏感数据做假名化保护

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Private Prompts** is an application designed to manage your AI prompts securely and locally on your device, ensuri
> L25:  Define what you consider sensitive data. The app can automatically mask confidential information before sending it
> L121:  - **Mark Sensitive Data**: Highlights confidential information in your prompt for further processing.

## 星数曲线

```mermaid
xychart-beta
    title "fboerncke/private-prompts-prototype 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-20"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-20 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `41fa30f9c52f` · [字段定义](../../DATASET.md)*
