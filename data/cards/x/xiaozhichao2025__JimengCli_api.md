# xiaozhichao2025/JimengCli_api

⭐ 52 · TypeScript · NOASSERTION · 推送 2026-04-23 · [GitHub](https://github.com/xiaozhichao2025/JimengCli_api) · 个人维护 · 中文 README

**将火山即梦 CLI 封装为 OpenAI 协议 API 的自建网关**

把火山即梦（Dreamina）官方 CLI 命令工具封装为符合 OpenAI 规范的 API 接口，支持 seedance2.0 等模型的生成任务调度，供现有工作流以标准 API 形式接入自己的即梦 VIP 账号并消耗即梦积分。提供管理后台：内部账号池（OAuth Device Flow 绑定）、API 令牌分发、任务状态管理与重试。关键限制：需自行下载官方 CLI（v1.4.2+）、必须持有即梦 VIP 账号、API 体验期至 2026 年 5 月 1 日，明确禁止商用滥用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 即梦 CLI 转 OpenAI 协议 API，支持 seedance2.0 与 VIP 调用
- 管理后台含账号池、API 令牌分发、任务管理与重试
- Windows 一键 start.bat 自动安装 Node.js 并拉取官方 CLI
- 任务 24h 超时自动失败与 logid 持久化追踪

## 适用场景

- 让自己的工作流通过标准 OpenAI API 调用即梦账号生成视频/图片
- 团队内分发 API 令牌、管理多个即梦 VIP 账号池
- 跟踪生成任务的实时状态与调试信息

## 场景标签

`模型网关` `视频生成` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L3: 本项目致力于将火山即梦底层的 CLI 命令工具，转化为符合 OpenAI / 标准规范的 API 接口，从而可以无缝接入到现有的任何工作流中（包含对 seedance2.0、VIP 调用的支持）。
> L61: 系统跑起来后，你需要进入管理后台绑定**即梦 VIP 账号** 和 **生成 API 令牌**。

## 星数曲线

```mermaid
xychart-beta
    title "xiaozhichao2025/JimengCli_api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-26 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `325c8c3f5ffb` · [字段定义](../../DATASET.md)*
