# manzolo/myshell-openvoice-docker

⭐ 40 · Dockerfile · 推送 2026-07-18 · [GitHub](https://github.com/manzolo/myshell-openvoice-docker) · 个人维护

**将 MyShell OpenVoice 语音转换工具打包为 Docker 镜像的封装项目**

一个为 OpenVoice（MyShell AI 的语音转换项目）提供 Docker 封装的个人项目：基于 Ubuntu 基础镜像构建容器，不修改上游应用代码，通过 docker build 构建镜像、docker run 映射 7860 端口后可在浏览器访问 OpenVoice 应用。README 声明仅负责打包，上游应用的 bug 需到上游仓库反馈，且与 MyShell AI 无隶属关系，作为个人爱好项目维护，不保证支持或及时更新。属于 manzolo Local AI Lab 自托管 AI 项目家族，可通过 local-ai-net Docker 网络互联。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 Ubuntu 基础镜像上封装 OpenVoice，不修改上游代码
- 构建后暴露 7860 端口，浏览器访问 Web 界面
- 属于 Local AILab 项目家族，可通过 local-ai-net 网络与其他自托管 AI 项目互联

## 适用场景

- 在 Docker 环境中运行 OpenVoice 而无需手动配置依赖
- 将语音转换服务纳入自托管 AI 项目组合统一管理

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L9: This project is a **Docker wrapper** for OpenVoice by MyShell AI. It provides a convenient way to run OpenVoice insi
> L13: > **Disclaimer:** This project is not affiliated with or endorsed by MyShell AI. It is maintained as a personal hob

## 星数曲线

```mermaid
xychart-beta
    title "manzolo/myshell-openvoice-docker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-25 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fba3cbabe3f3` · [字段定义](../../DATASET.md)*
