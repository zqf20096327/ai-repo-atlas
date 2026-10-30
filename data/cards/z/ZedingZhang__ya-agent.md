# ZedingZhang/ya-agent

⭐ 23 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/ZedingZhang/ya-agent) · 个人维护 · 中文 README

**专为 DeepSeek 打造的命令行与桌面端 coding agent**

用 TypeScript 编写的共享核心同时提供 CLI 与 Electron 桌面应用，默认调用 DeepSeek API（DeepSeek-V4.1-Flash，可切换 V4-Pro），支持平台账号浏览器 PKCE 登录或 API key。机制上：SEA 通过显式用户反馈生成候选记忆卡、仅批准后生效；ICM 对标注的证据缺口做至多一次追问；有界 Tree of Agents 用根协调者加至多两个临时 worker。命令执行、ToA 启动均需逐任务批准；本地模式仅限单一 workspace 的受限文件工具。支持视觉输入（JPEG/PNG/GIF/WebP）与代码验证闭环。发布 tarball 提供三平台独立二进制；v0.8.0 Windows 安装有已知启动故障，README 建议改用源码安装。

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

- SEA 自我进化：显式反馈生成候选记忆卡，仅批准后影响后续任务
- 有界 Tree of Agents：根协调者 + 至多 2 个临时 worker，带 token/超时上限
- 视觉输入直发 deepseek-flash，支持本地文件/URL/base64/Files API ID
- CLI 与 Electron 桌面端共享同一类型化服务层，凭据走 Keychain 或受限存储

## 适用场景

- 在终端或桌面以对话方式做编码与分析任务
- 经用户批准后让 agent 在单一 workspace 内读写文件并跑测试修复
- 用 ToA 模式做多 worker 的决策与证据研究

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: Ya (丫丫) is a coding agent built specifically for DeepSeek, with a command-line interface and a native desktop applic
> L7: Ya uses the DeepSeek API (`DeepSeek-V4.1-Flash` by default, with the option to switch to `DeepSeek-V4-Pro-0813`), st
> L17: - **SEA controlled learning:** explicit user feedback becomes a candidate memory card. Only approved cards can infl

## 星数曲线

```mermaid
xychart-beta
    title "ZedingZhang/ya-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-30 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `38c1c82e8b11` · [字段定义](../../DATASET.md)*
