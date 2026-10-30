# stefanoginella/aicontainer

⭐ 21 · Shell · MIT · 推送 2026-10-28 · [GitHub](https://github.com/stefanoginella/aicontainer) · [官网](https://www.npmjs.com/package/aicontainer) · 个人维护

**沙箱化 devcontainer：安全运行开启自动批准的 AI 编程 CLI**

面向在 bypass / auto-approve 模式下使用 Claude Code、Codex、OpenCode 的开发者，通过 devcontainer 边界隔离 AI 代理：仅项目目录可写，宿主 home、~/.ssh 与凭据不进容器；宿主配置经无网络净化器过滤后传入；Docker 对象默认不可访问，digest 固定的 socket proxy 仅放行 ping/version；云元数据与链路本地地址默认阻断；PreToolUse 钩子拒绝明显 .env 读取与 curl | sh。以 npm CLI（aic）形式提供，需 Docker Engine 25+ 与 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文件系统隔离：项目目录为唯一可写路径，宿主凭据不入容器
- 默认禁止 Docker 对象访问，digest 固定 socket proxy 可选升级为只读/读写
- 宿主 Git 与工具配置经无网络净化器仅传白名单字段
- 共享 PreToolUse 钩子在三种工具中拒绝 .env 读取与 curl | sh

## 适用场景

- 让 AI 编程 CLI 保持自动批准模式的同时限制其对宿主的破坏面
- 多项目间共享登录 token 但保留各自会话与记忆
- 防止 prompt 注入的依赖读取 .env 或滥用 gh token

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: A sandboxed devcontainer for Claude Code,
> L14: **Why?** These CLIs work best with auto-approve on. But on your real `$HOME`,
> L16: or push with your `gh` token. aicontainer puts the AI behind a devcontainer

## 星数曲线

```mermaid
xychart-beta
    title "stefanoginella/aicontainer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `e2a415a8d8ee` · [字段定义](../../DATASET.md)*
