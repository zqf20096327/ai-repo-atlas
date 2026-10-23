# MadeAgents/mobile-use

⭐ 242 · Python · MIT · 推送 2026-07-10 · [GitHub](https://github.com/MadeAgents/mobile-use) · [官网](https://arxiv.org/abs/2507.16853) · 组织维护 · 中文 README

**安卓真机自动化 GUI agent：用多模态大模型完成长程手机任务**

开源移动 GUI agent，通过 ADB 控制真实安卓设备：解析 GUI 布局识别操作目标，结合多模态 LLM/VLM、层级反思、主动探索与多 agent 框架（规划/反思/记忆/进度）完成跨应用的长程任务。提供 WebUI（Gradio）、Python API 与 AndroidWorld/AndroidLab 基准评测流程；需自行配置 VLM 的 Base URL 与 API Key，推荐 Qwen2.5-VL 系列。安装前置为 SDK Platform-Tools（ADB）与手机 USB 调试连接，输入中文需额外安装 ADBKeyBoard。README 提示 agent 自主决策存在不可控操作风险，建议使用测试机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 ADB 控制真实安卓设备，自动解析 GUI 布局并执行任务
- 多 agent 框架：规划、反思、记忆与进度机制
- 支持 AndroidWorld 与 AndroidLab 基准评测
- 提供 WebUI 与 Python API 两种使用方式

## 适用场景

- 用自然语言任务描述让 agent 代为操作手机完成点餐、搜索等跨应用任务
- 在 AndroidWorld/AndroidLab 基准上评测移动 agent 能力
- 以 Python API 将手机自动化集成到自己的程序中

## 场景标签

`GUI 自动化` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: MobileUse is an open-source mobile GUI agent that controls real Android devices through ADB. It uses multimodal LLMs
> L92: Click VLM Configuration to set the Base URL and API Key of the multimodal large language model. It is recommended t

## 星数曲线

```mermaid
xychart-beta
    title "MadeAgents/mobile-use 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 236 --> 243
    line [237, 239, 242]
```

2026-10-18 237 → 2026-10-23 242（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `899602290f28` · [字段定义](../../DATASET.md)*
