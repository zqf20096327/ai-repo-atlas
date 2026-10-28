# coder/httpjail

⭐ 961 · Rust · CC0-1.0 · 推送 2026-09-24 · [GitHub](https://github.com/coder/httpjail) · 组织维护

**进程级 HTTP/HTTPS 请求过滤工具：默认拒绝、按规则放行**

跨平台命令行工具，通过网络隔离与透明代理拦截监控并限制进程发出的 HTTP/HTTPS 请求。默认拒绝所有网络请求，需提供 JS 表达式或自定义程序作为规则来放行流量；支持 TLS 证书注入的 HTTPS 拦截、DNS 渗出防护、请求日志。Linux/macOS 原生支持，Linux 强模式基于 sudo/nft/seccomp/PID namespace 实现隔离，另有 Docker 模式。自声明为实验性，不保证 API/CLI 兼容性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 默认拒绝所有网络请求，由 JS 表达式或自定义程序决定放行
- 透明代理拦截 HTTPS（TLS 证书注入）与 DNS 渗出防护
- Linux 强模式：私有 PID namespace、seccomp、no_new_privs
- Docker 模式仅接受受限的 docker run 标志，远程上下文被忽略

## 适用场景

- 沙箱化运行不受信任的程序，限制其对外网络访问
- 为 AI agent 或自动化脚本的网络出站流量设置白名单
- 审计进程发出的完整 HTTP/HTTPS 请求并记录日志

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: A cross-platform tool for monitoring and restricting HTTP/HTTPS requests from processes using network isolation and 
> L22: - 🔒 **Process-level network isolation** - Isolate processes in restricted network environments
> L25: - 🔧 **Multiple evaluation approaches** - JS expressions or custom programs

## 星数曲线

```mermaid
xychart-beta
    title "coder/httpjail 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 960 --> 962
    line [961, 961]
```

2026-10-18 961 → 2026-10-28 961（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 low · 依据 README sha `796970fad857` · [字段定义](../../DATASET.md)*
