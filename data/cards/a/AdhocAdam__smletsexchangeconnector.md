# AdhocAdam/smletsexchangeconnector

⭐ 28 · C# · GPL-3.0 · 推送 2026-09-23 · [GitHub](https://github.com/AdhocAdam/smletsexchangeconnector) · [官网](https://adhocadam.github.io/smletsexchangeconnector/) · 个人维护

**面向 SCSM 管理员的开源 Exchange 连接器 PowerShell 脚本**

基于 SMLets 模块的 PowerShell 脚本，替代 System Center Service Manager 原生 Exchange Connector 5.0，通过 Exchange 邮箱处理工作项更新（创建/审批/关闭等关键词操作），支持 Exchange Online 的 Microsoft Graph 与 OAuth 2.0、多邮箱处理、自定义规则、120+ 配置项及设置管理包。AI 为可选功能：集成 Azure 语音转写、图像描述与 OCR、翻译、情感分析驱动的动态优先级、Azure Machine Learning 的工单分类路由与受影响配置项预测。面向熟悉 PowerShell 与 SMLets 的 SCSM 管理员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 复刻 Exchange Connector 5.0 全部功能并支持 Exchange Online 的 Microsoft Graph v6.0 与 OAuth 2.0
- Azure Cognitive Services 集成：语音转写、图像描述/OCR、情感分析驱动优先级、翻译
- Azure Machine Learning 训练模型自动完成工单类型/分类/支持组选择与受影响配置项预测
- 多邮箱多模板处理、自定义规则同步外部系统、120+ 配置项

## 适用场景

- SCSM 部署通过邮箱自动创建和更新工单
- 多语言环境下用邮件关键词审批 Review Activity
- 把外部工单系统/告警工具邮件同步为 Service Manager 工作项
- 利用 Azure AI 对邮件附件转写、识别图像并自动分类路由工单

## 场景标签

`语音识别` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L12: This PowerShell script leverages the SMLets module to build an open and flexible Exchange Connector for controlling
> L15: The stock Exchange Connector is a seperate download that enables SCSM deployments to leverage an Exchange mailbox t

## 星数曲线

```mermaid
xychart-beta
    title "AdhocAdam/smletsexchangeconnector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-27 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9fd7efd96f7c` · [字段定义](../../DATASET.md)*
