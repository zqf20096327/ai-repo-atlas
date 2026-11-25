# ItsWendell/palot

⭐ 195 · TypeScript · MIT · 推送 2026-11-04 · [GitHub](https://github.com/ItsWendell/palot) · 个人维护

**为 OpenCode 2 提供跨会话与变更管理的桌面客户端**

面向 Linux 与 macOS 的独立桌面客户端，连接本机 OpenCode 服务（该服务为项目、会话、消息与工具执行的数据源），提供多会话并行管理、活动与代码变更审查、请求处理、本地连接管理等功能。支持 GitHub 风格 Markdown 渲染、文件树浏览、PR 生成、定时任务与自定义主题。安装方式包括 AppImage/RPM/DEB/DMG 或从源码构建（需 Bun/Node/Vite+），安装包为实验性 pre-release，macOS 下载为 ad-hoc 签名，更新需手动进行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 跨项目/会话/并行 agent 的统一桌面界面与变更审查
- 从 Changes 生成描述创建 PR，支持 GitLab merge request
- 通过 npm/Bun/pnpm/Yarn/curl 管理 OpenCode 运行时版本
- 从源码构建（Bun 1.4.4、Node.js 24+、Vite+）

## 适用场景

- 在桌面上并行管理多个 OpenCode agent 会话
- 审查 agent 产生的代码变更并发起 Pull Request
- 管理本机 OpenCode 服务的启动、升级与恢复

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: Palot is an independent desktop client for OpenCode 2 on Linux and macOS. It is not
> L9: Palot keeps OpenCode as the source of truth for projects, sessions, messages,
> L141: **2.x starting at 2.0.7** is supported as an external service; the client and

## 星数曲线

```mermaid
xychart-beta
    title "ItsWendell/palot 星数(近 6 点)"
    x-axis ["2026-10-23", "2026-10-30", "2026-11-06", "2026-11-08", "2026-11-22", "2026-11-25"]
    y-axis "stars" 191 --> 196
    line [192, 193, 192, 194, 195, 195]
```

2026-10-23 192 → 2026-11-25 195（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `485167a89a0c` · [字段定义](../../DATASET.md)*
