# kasemjeff/aipass-desktop

⭐ 4 · JavaScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/kasemjeff/aipass-desktop) · [官网](https://kasemjeff.github.io/aipass-desktop/) · 个人维护

**面向 de.aipass.net 用户的本地优先 AI 编码代理桌面端与 harness**

为 de.aipass.net 文件编辑代理提供的桌面窗口与 agent harness，通过 Chrome 扩展经用户已登录的浏览器标签访问站点，凭据不离开浏览器。核心流程为四步：发送任务（泰/英文）、逐行查看工具调用、按文件审阅 diff、勾选批准后才写入。会话可暂停与恢复，编辑在批准前保持暂存。Tauri + Node 实现，零 npm 运行时依赖，当前为 pre-1.0，仅可从源码安装，原生包仅在 Windows 上验证。非官方客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 逐文件 diff 审阅与勾选批准机制，未经批准不写入
- 通过浏览器标签与 Chrome 扩展访问服务，凭据不复制出浏览器
- 会话可恢复（resume），本地状态存于 ~/.aipass/
- 零 npm 运行时依赖，无需 API key 与数据库

## 适用场景

- 以泰语或英语下发编码任务并逐文件审批改动
- 在桌面窗口中查看与恢复代理编码会话
- 希望凭据保留在浏览器内、不经 API key 的使用方式

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L8: > **The desktop window and agent harness for de.aipass.net** — a file-editing agent you can watch, approve and resum
> L39: |**3. Review the diff**|Edits pile up in a pending panel — real per-file diffs, not a summary|Tick only the files y
> L121: No. An independent community project that talks to `de.aipass.net` through your own

## 星数曲线

```mermaid
xychart-beta
    title "kasemjeff/aipass-desktop 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-08 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ac8921b98f90` · [字段定义](../../DATASET.md)*
