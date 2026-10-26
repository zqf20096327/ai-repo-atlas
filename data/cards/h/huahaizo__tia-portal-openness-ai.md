# huahaizo/tia-portal-openness-ai

⭐ 77 · PowerShell · 推送 2026-05-24 · [GitHub](https://github.com/huahaizo/tia-portal-openness-ai) · 个人维护 · 中文 README

**让 AI 通过 Openness API 自动化操作西门子博途项目的 skill 与 C# 脚手架**

面向 TIA Portal V15-V21 的 AI skill（SKILL.md）加 C# 控制器脚手架：用户以中文描述需求（如打开项目、导出/导入 PLC 块、编译、归档），AI 生成可审查的动作计划，再由 PowerShell 脚本生成的 C# 控制器调用 Siemens.Engineering 官方 API 执行。脚手架已处理 DLL 加载顺序问题（先注册程序集解析器）。要求 Windows、本机安装 TIA Portal、用户加入 Siemens TIA Openness 用户组；需自备 Siemens 授权软件，项目与 Siemens 无隶属关系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言需求 → AI 动作计划 → JSON/YAML 指令 → C# Openness 控制器的执行链路
- PowerShell 脚本自动扫描本机 Openness API 并生成 C# 控制器骨架
- 支持 TIA Portal V15 至 V21，默认选用最高可用版本
- 内置程序集解析器注册，规避 Siemens.Engineering.dll 常见加载错误

## 适用场景

- 让 AI 打开博途项目并列出设备、导出 PLC 块
- 把 AI 生成的 SCL 源文件导入项目并编译、获取诊断信息
- 归档与批量管理 TIA Portal 项目的自动化操作

## 场景标签

`代码生成` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: 你可以用中文描述需求，例如“打开项目并列出所有设备”“导出 PLC 块”“把这段 SCL 导入项目并编译”。AI 会先生成可审查的动作计划，再通过 C# 控制器调用 `Siemens.Engineering` 官方 API 执行。
> L13: 你的需求 -> AI 动作计划 -> JSON/YAML 指令 -> C# Openness 控制器 -> TIA Portal 项目
> L50: 把整个 `tia-openness-control` 文件夹复制到你的 AI 工具或 Agent 支持的 skills 目录中。这个文件夹必须包含 `SKILL.md`。

## 星数曲线

```mermaid
xychart-beta
    title "huahaizo/tia-portal-openness-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 76 --> 78
    line [77, 77]
```

2026-10-18 77 → 2026-10-26 77（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a6c5c7f647c8` · [字段定义](../../DATASET.md)*
