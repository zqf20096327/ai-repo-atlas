# dongsheng123132/u-claw-linux

⭐ 14 · PowerShell · MIT · 推送 2026-10-03 · [GitHub](https://github.com/dongsheng123132/u-claw-linux) · 个人维护 · 中文 README

**可启动 Linux AI 工作站 U 盘：插盘开机即用 AI 助手**

制作可启动 Linux U 盘的工具集：在 Windows 上经 4 个 PowerShell 脚本完成 Ventoy 写入、Ubuntu 24.04 ISO 下载（国内镜像）、casper-rw ext4 持久化镜像创建与文件拷贝；目标电脑无需任何操作系统，从 U 盘启动进入 Ubuntu 桌面后一键安装 OpenClaw AI 助手（含 QQ 插件），数据保存于持久化分区。限制：需 32GB+ U 盘（推荐 USB 3.0）、制作环境为 Windows 10/11、首次安装 OpenClaw 需联网、部分电脑需关闭 Secure Boot、AI 推理在云端进行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ventoy + Ubuntu 24.04 + casper-rw 持久化的 Live USB 方案，目标电脑无需已有系统
- setup-openclaw.sh 九步安装 OpenClaw 及桌面快捷方式
- ISO 与 Node.js 下载默认走清华/阿里/中科大国内镜像，SHA256 校验
- 重启后软件与数据保留，除非重新格式化 U 盘

## 适用场景

- 在没有系统或不想安装系统的电脑上临时获得 AI 工作环境
- 随身携带可持久化的 Linux + AI 助手环境，换机即用
- 国内网络环境下无翻墙制作与使用

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L30: - 插上任意电脑，从 U 盘启动，直接进入 Ubuntu 桌面
> L31: - 一键安装 OpenClaw AI 助手，桌面图标双击即用
> L278:  - AI 推理在云端，本地只跑网关，所以 AI 对话速度不受影响

## 星数曲线

```mermaid
xychart-beta
    title "dongsheng123132/u-claw-linux 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `2b7b893d9d48` · [字段定义](../../DATASET.md)*
