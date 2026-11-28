# huxc573/workbuddy2api-panel-magisk

⭐ 3 · Shell · MIT · 推送 2026-11-27 · [GitHub](https://github.com/huxc573/workbuddy2api-panel-magisk) · 个人维护 · 中文 README

**把 WorkBuddy2API Panel 打包为 Android root 模块：开机自启+崩溃拉起**

本仓库是安装壳而非服务本体：上游 misakano7545/workbuddy2api-panel（Go 单静态二进制）由 CI 从其 release 原样取出打包为 Magisk/APatch/KernelSU 模块，提供开机自启、wait 式看门狗崩溃拉起、跟随上游 release 的自动更新与 update.json 检查机制。针对 Android 环境补齐 DNS、Mozilla 根证书、时区三件事，支持音量键交互式安装配置或 5 秒免配置默认值，提供 action.sh 密钥查看与进程重启等管理命令。安装方式为 Releases 下载 zip 刷入，首次安装需重启；仅支持 arm64。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Magisk/APatch/KernelSU 三类管理器通用，开机自启+看门狗崩溃拉起
- CI 跟随上游 release 自动打包发版，update.json 支持管理器内更新
- 补齐 Android 缺失的 DNS、根证书、tzdata 三项运行环境
- 音量键交互配置，5 秒无按键取默认免配置

## 适用场景

- 在已 root 的 Android arm64 手机上以服务方式常驻运行 WorkBuddy2API Panel
- 需要进程崩溃后自动重启与开机自启的部署
- 国内网络下多源下载自动跟随上游更新

## 场景标签

 · 领域:Android root 工具/部署自动化

## 证据(README 行号)

> L3: 在 Android（arm64）上把 WorkBuddy2API Panel 跑成开机自启的 Magisk 模块。
> L10: > **上游与致谢**：服务本体、Web 面板、账号池与任务体系全部来自
> L12: > 本项目只做「把它装进 Android」这层壳——数据目录布局、启动/看门狗、Android 特有的三件套


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `50ddc28a87ee` · [字段定义](../../DATASET.md)*
