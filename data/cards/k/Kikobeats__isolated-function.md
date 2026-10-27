# Kikobeats/isolated-function

⭐ 23 · JavaScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Kikobeats/isolated-function) · [官网](https://isolated-function.js.org/) · 个人维护

**在独立 Node.js 进程中受控执行用户自定义 JavaScript 的沙箱库**

面向需要让用户提供自定义逻辑（AI agent 函数模板、插件、workflow、webhook 转换）的应用：把 JavaScript 函数包装后在独立 Node.js 子进程中执行，通过 Node.js Permission Model 限制文件系统、网络、worker 与子进程访问，并施加内存（V8 堆）、墙钟与 CPU 时间限制。自动解析 require/import、经 upm 进程内安装依赖并用 esbuild 打包，支持依赖白名单与跨调用复用；返回结果、日志、错误及分阶段 profiling 数据。明确声明不是 VM/微虚拟机/容器级隔离，多租户敌意代码需外层更强边界。以 npm 包提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 独立进程 + Node.js Permission Model 的最小权限执行，越权操作直接失败
- 内存（V8 堆）、墙钟、CPU（RLIMIT_CPU/SIGXCPU）三类资源限制
- 依赖自动检测、upm 进程内安装（不执行生命周期脚本）、esbuild 打包与共享缓存复用
- 返回 compile/spawn/run 分阶段 profiling 与日志、错误传播

## 适用场景

- 让 AI agent 在受控沙箱中运行用户提供的函数模板
- 产品中开放插件/workflow/webhook 自定义逻辑而不暴露宿主环境
- 对不受信任代码施加依赖白名单与资源限额后执行

## 场景标签

 · 领域:开发者工具/代码沙箱

## 证据(README 行号)

> L19: Sometimes your application needs to let users customize a piece of behavior with JavaScript.
> L44: - run untrusted code in a separate process
> L45: - restrict filesystem, network, worker, and child-process access through the Node.js Permission Model

## 星数曲线

```mermaid
xychart-beta
    title "Kikobeats/isolated-function 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `cefad9783607` · [字段定义](../../DATASET.md)*
